from django import forms
from portal.models import Category


class ProductForm(forms.Form):
    name = forms.CharField(
        label='Nome',
        max_length=244,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nome'

        })
    )

    category = forms.ModelChoiceField(
        label='Categoria',
        queryset=Category.objects.all(),
        empty_label='-----',
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    quantity = forms.CharField(
        label='Quantidade',
        max_length=4,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Quantidade'

        })
    )
    price = forms.CharField(
        label='Valor',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Valor'

        })
    )
    short_description = forms.CharField(
        label='Descrição Curta',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Descrição Curta'

        })
    )
    description = forms.CharField(
        label='Descrição',
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Descrição'

        })
    )
