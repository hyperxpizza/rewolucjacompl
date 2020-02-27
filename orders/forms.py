from django import forms
from .models import Order

class OrderForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True
        self.fields['phone'].required = True
        self.fields['adress'].required = True
        self.fields['postal_code'].required = True
        self.fields['city'].required = True
    
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone', 'adress', 'postal_code', 'city',]