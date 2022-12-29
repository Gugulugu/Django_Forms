from .models import Booking
from django.forms import Form

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"