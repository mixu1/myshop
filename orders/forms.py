from django import forms

from localflavor.cn.forms import CNPostCodeField

from .models import Order


class OrderCreateForm(forms.ModelForm):
    postal_code = CNPostCodeField()

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address',
                  'postal_code', 'city']
