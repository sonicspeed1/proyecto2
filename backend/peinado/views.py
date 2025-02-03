from rest_framework import viewsets
from .models import Peinado
from .serializers import PeinadoSerializer

class PeinadoViewSet(viewsets.ModelViewSet):
    queryset = Peinado.objects.all()
    serializer_class = PeinadoSerializer