from rest_framework import viewsets
from .models import ManicuraPedicura
from .serializers import ManicuraPedicuraSerializer

class ManicuraPedicuraViewSet(viewsets.ModelViewSet):
    queryset = ManicuraPedicura.objects.all()