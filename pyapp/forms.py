from django import forms
from pyapp.models import MyModel
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
class phoneform(forms.ModelForm):
    phone_number=PhoneNumberField(
        widget=PhoneNumberPrefixWidget(initial='IN')
    )
    class Meta:
        model = MyModel
        fields = ('__all__')
    