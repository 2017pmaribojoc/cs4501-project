__author__ = 'Patrick'
# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from homepage.models import Baby, Daddy

class BabySerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)
    id = serializers.IntegerField()
    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return Baby.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.id = validated_data.get('id', instance.id)

        instance.save()
        return instance

class DaddySerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)
    id = serializers.IntegerField()
    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return Daddy.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.id = validated_data.get('id', instance.id)

        instance.save()
        return instance