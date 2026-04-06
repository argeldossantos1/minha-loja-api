from django.urls import path, include
from rest_framework import routers
from .views import SocialnetworkViewSet

app_name = 'socialnetworks'

router = routers.SimpleRouter()
router.register('', SocialnetworkViewSet, basename='socialnetworks')

urlpatterns = [
    path('', include(router.urls)),
]