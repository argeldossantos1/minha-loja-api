from django.urls import path, include
from rest_framework import routers
from .views import PersonViewSet

app_name = 'persons'

router = routers.SimpleRouter()
router.register('', PersonViewSet, basename='persons')

urlpatterns = [
    path('', include(router.urls)),
]