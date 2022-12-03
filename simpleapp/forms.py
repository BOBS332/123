from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from .models import Product


User = get_user_model()


class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=100, required=True, label='Имя пользователя')
    password = forms.CharField(max_length=100, required=True, label='Пароль', widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=100, required=True, label='Повторите пароль', widget=forms.PasswordInput())


class ProductForm(forms.ModelForm):
    description = forms.CharField(min_length=20)

    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price', 'quantity']

    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get("description")
        name = cleaned_data.get("name")

        if name == description:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

        return cleaned_data