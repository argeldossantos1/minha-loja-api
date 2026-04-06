from rest_framework import viewsets
from .models import Socialnetwork
from .serializer import SocialnetworkSerializer

class SocialnetworkViewSet(viewsets.ModelViewSet):
    queryset = Socialnetwork.objects.all()
    serializer_class = SocialnetworkSerializer