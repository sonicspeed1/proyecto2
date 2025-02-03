from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PeinadoViewSet

router = DefaultRouter()
router.register(r'peinados', PeinadoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]