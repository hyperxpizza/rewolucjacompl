from django import forms
from website.models import Order

class NewSubscriberForm(forms.Form):
    email = forms.EmailField(label='Your email', max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control'}))

class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True
        self.fields['phone'].required = True
        self.fields['address_line_1'].required = True
        self.fields['address_line_2'].required = False
        self.fields['sip_code'].required = True
        self.fields['city'].required = True
        self.fields['country'].required = True
    
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone', 'address_line_1', 'address_line_2', 'zip_code', 'city','country']