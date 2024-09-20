from django import forms


class SignUpForm(forms.Form):
    username = forms.CharField(label="Your username", max_length=100)
    first_name = forms.CharField(label="Your first name", max_length=100)
    last_name = forms.CharField(label="Your last name", max_length=100)
    email = forms.EmailField(label="Your email")

    password = forms.CharField(
        label="Your password", max_length=100, widget=forms.PasswordInput
    )
    confirm_password = forms.CharField(
        label="Re-enter password", max_length=100, widget=forms.PasswordInput
    )


class LoginForm(forms.Form):
    username = forms.CharField(label="Your username")
    password = forms.CharField(
        label="Your password", max_length=100, widget=forms.PasswordInput
    )
