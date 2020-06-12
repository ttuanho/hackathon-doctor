from django.urls import path, include
from rest_framework.routers import DefaultRouter

from doctor import views


router = DefaultRouter()
router.register('tags', views.TagViewSet)

app_name = 'doctor'

urlpatterns = [
    path('', include(router.urls))
]