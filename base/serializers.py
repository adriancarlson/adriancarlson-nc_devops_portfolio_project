from rest_framework import serializers
from .models import  Parishes, Intentions, Meetings


class IntentionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intentions
        fields = ('id', 'intention', 'category', 'requestor', 'requestor_email', 'requestor_phone', 'donation_amount', 'status')