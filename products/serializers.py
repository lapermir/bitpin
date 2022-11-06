from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Product, Rate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'token')

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
            return instance


class ScoreSerializer(ModelSerializer):
    class Meta:
        model = Rate
        fields = ['score']

class ProductSerializer(ModelSerializer):
    score = ScoreSerializer()
    class Meta:
        model = Product
        fields = ['title', 'description', 'score']


class ProductEditSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'score']