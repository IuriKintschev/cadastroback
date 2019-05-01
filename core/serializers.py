from rest_framework import serializers
from .models import Name

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Name
        fields = ('nome', 'telefone', 'email')