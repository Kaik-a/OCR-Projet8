from django import forms


class LoginForm(forms.Form):
    """Class to create form for user."""
    login = forms.CharField(label="Nom d'utilisateur", max_length=100)
    password = forms.CharField(label="Mot de passse", widget=forms.PasswordInput)


class SubscribeForm(forms.Form):
    """Class to create from for creating user."""
    login = forms.CharField(label="Nom d'utilisateur", max_length=100)
    email = forms.EmailField(label="E-mail")
    password = forms.CharField(label="Mot de passse", widget=forms.PasswordInput)
    confirm_password = forms.CharField(
        label="Confirmer le mot de passe", widget=forms.PasswordInput
    )
    first_name = forms.CharField(label="Prénom", max_length=50)
    last_name = forms.CharField(label="Nom", max_length=120)

    def clean(self):
        cleaned_data = super(SubscribeForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Les deux mots de passe ne correspondent pas"
            )
