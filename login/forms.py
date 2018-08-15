from django import forms

class RegistrationForm(forms.Form):
    username = forms.RegexField(
        regex=r'^\w+$',
        widget=forms.TextInput(
            attrs=dict(required=True,
                       max_length=30,
                       label='Usuário',
                       error_messages={
                           'invalid': 'Usuário pode conter apenas letras e números'
                           }
                       )
            )
        )
