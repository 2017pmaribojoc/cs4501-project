__author__ = 'Patrick'
# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from homepage.models import User
#
# class UserSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=20)
#     second_name = serializers.CharField(max_length=20)
#
#     def create(self, validated_data):
#         """
#         Create and return a new `User` instance, given the validated data.
#         """
#         return User.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.second_name = validated_data.get('second_name', instance.second_name)
#
#         instance.save()
#         return instance

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'id')