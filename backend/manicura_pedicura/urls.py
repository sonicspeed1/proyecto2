from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ManicuraPedicuraViewSet

router = DefaultRouter()
router.register(r'manicura_pedicura', ManicuraPedicuraViewSet)

urlpatterns = [
    path('', include(router.urls)),
]