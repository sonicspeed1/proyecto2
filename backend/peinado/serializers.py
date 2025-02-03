from rest_framework import serializers
from .models import Peinado

class PeinadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peinado
        fields = '__all__'