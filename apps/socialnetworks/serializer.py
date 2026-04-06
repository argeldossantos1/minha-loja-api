from rest_framework import serializers
from .models import Socialnetwork

class SocialnetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socialnetwork
        fields = '__all__'