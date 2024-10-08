from .models import Register
from rest_framework import serializers

class RegisterAllUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = "__all__"