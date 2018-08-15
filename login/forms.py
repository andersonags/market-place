from django import forms

class RegistrationForms(forms.Form):
    username = forms.RegexField(
        regex=r'^\w+$',
        widget=forms.TextInput(
            attrs=dict(riquired-True,
                       max_length=30,
                       label='Usuário',
                       error_messages={
                           'invalid': 'Usuário pode conter apenas letras e números'
                           }
                       )
            )
        )
