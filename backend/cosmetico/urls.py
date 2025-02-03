from django.urls import path
from .views import CosmeticoListCreateAPIView, CosmeticoDetailAPIView

urlpatterns = [
    path('cosmeticos/', CosmeticoListCreateAPIView.as_view(), name='cosmetico-list-create'),
    path('cosmeticos/<int:pk>/', CosmeticoDetailAPIView.as_view(), name='cosmetico-detail'),
]