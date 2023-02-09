from abc import ABC
from datetime import datetime

from .models import Room, Message
from rest_framework import serializers


class RoomSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=1000)

    class Meta:
        model = Room
        fields = ['name']

        def Create(self, validated_data):
            return Room.objects.create(**validated_data)


class MessageSerializer(serializers.Serializer):


    class Meta:
        model = Message
        fields = ["value", "date", "user", "room"]

        def Create(self, validated_data):
            return Message.objects.create(**validated_data)