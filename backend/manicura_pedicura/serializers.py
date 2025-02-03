from rest_framework import serializers
from .models import ManicuraPedicura

class ManicuraPedicuraSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManicuraPedicura
        fields = '__all__'