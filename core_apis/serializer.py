from rest_framework import serializers
from .models import MyDemo


class MyAPI(serializers.ModelSerializer):

    class Meta:
        model = MyDemo
        fields = '__all__'