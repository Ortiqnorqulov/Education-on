from django import forms
from order.models import CourseCarts, Order


class CoursecartForm(forms.ModelForm):
    class Meta:
        model = CourseCarts
        fields = ('user', 'name', 'phone', 'email', 'country', 'city', 'title', 'price', 'image',)

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'address', 'phone', 'email', 'city', 'country','feedback',]