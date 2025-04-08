from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'phone']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите ваше ФИО'
        })
        self.fields['phone'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите ваш номер телефона'
        })

class PriceFilterForm(forms.Form):
    min_price = forms.DecimalField(
        label='Мин. цена',
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'От'})
    )
    max_price = forms.DecimalField(
        label='Макс. цена',
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'До'})
    )