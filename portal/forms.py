from django import forms


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
    quantity = forms.CharField(
        label='Quantidade',
        max_length=4,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Quantidade'

        })
    )
    prince = forms.CharField(
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
        max_length=4,
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Descrição'

        })
    )
