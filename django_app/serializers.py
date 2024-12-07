from rest_framework import serializers
from .models import User, EmailMessage

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'firstname', 'lastname']


class EmailMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailMessage
        fields = ['id', 'subject', 'message', 'recipients', 'created_at']
