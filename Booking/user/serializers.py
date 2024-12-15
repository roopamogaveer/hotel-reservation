from rest_framework import serializers
from .models import User


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('email','password','username')

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('email','password')