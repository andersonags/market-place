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
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs=dict(
                required=True,
                max_length=30
            )
        ),
        label='Email'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs=dict(
                required=True,
                max_length=30,
                render_value=False
            )
        ),
        label='Password'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs=dict(
                required=True,
                max_length=30,
                render_value=False
            )
        ),
        label='Repeat your password'
    )
