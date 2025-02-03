from rest_framework import serializers
from .models import Cosmetico

class CosmeticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cosmetico
        fields = '__all__'