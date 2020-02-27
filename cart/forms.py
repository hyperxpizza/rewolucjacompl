from django import forms
from store.models import Product

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1,11)]
SHIPPING_CHOICES = ["Za pobraniem"]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    #shipping = forms.TypedChoiceField(choices=SHIPPING_CHOICES)