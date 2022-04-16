from django.forms import ModelForm
from .models import Parishes, Intentions, Meetings

class ParishesForm(ModelForm):
    class Meta:
        model = Parishes
        fields = ['name', 'street', 'city', 'state', 'zip', 'diocese']

class IntentionsForm(ModelForm):
    class Meta:
        model = Intentions
        fields = ['intention', 'category', 'requestor', 'requestor_email', 'requestor_phone', 'donation_amount', 'status']

class  MeetingsForm(ModelForm):
    class Meta:
        model = Meetings
        fields = ['day', 'time', 'parish']