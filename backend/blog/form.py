from django import forms
from blog.models import Article, Categorie, Commentaire
from django_ckeditor_5.widgets import CKEditor5Widget

class InfosGeneralesForm(forms.ModelForm):
    couverture = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    categorie_id = forms.ModelChoiceField(
        queryset=Categorie.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Article
        fields = ['titre', 'categorie_id', 'tag_ids', 'couverture']

        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre de l\'article'}),
            'tag_ids': forms.SelectMultiple(attrs={'class': 'form-control'}),  # ✅ Correction ici
        }


class ContenuForm(forms.ModelForm):
    class Meta:

        model = Article
        fields = ['contenu']

        widgets = {
              "contenu": CKEditor5Widget(
                  attrs={"class": "django_ckeditor_5"}, config_name="extends"
              )
          }



class StandardsForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['statut']

        widgets = {
            'statut': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['contenu']
        labels = {
            'contenu': 'Votre commentaire',
        }
        widgets = {
            'contenu': forms.Textarea(attrs={
                'class': 'w-full h-24 px-4 py-2 text-lg border rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 placeholder-gray-400',
                'placeholder': 'Écrivez votre commentaire ici...',
                'rows': 4,
                'cols': 50,
            }),
        }
        error_messages = {
            'contenu': {
                'required': 'Le champ commentaire est requis.',
                'max_length': 'Le commentaire est trop long.',
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['contenu'].widget.attrs.update({
            'required': True,  # Ajoute l'attribut HTML required
        })
