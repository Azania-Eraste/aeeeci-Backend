from rest_framework import viewsets
from .models import CustomUser, ScoutUser
from .serializers import CustomSerializer, ScoutSerializer

class CustomViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomSerializer

class ScoutViewSet(viewsets.ModelViewSet):
    queryset = ScoutUser.objects.all()
    serializer_class = ScoutSerializer
