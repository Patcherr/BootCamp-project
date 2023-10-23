from django import forms
from clients.models import ClientModel

class SignUpForm(forms.ModelForm):
    """ username = forms.CharField()
    first_name = forms.CharField() 
    last_name = forms.CharField()
    password = forms.CharField()
    email = forms.CharField()
    cuit = forms.CharField(max_length=11)
    phone_number = forms.CharField
    business_line = forms.CharField()
    business_line_interes = forms.CharField()  
    is_buyers = forms.BooleanField()
    is_sellers = forms.BooleanField() """

    class Meta:
        model = ClientModel
        fields = ["first_name", "last_name", "password", "email"]



    