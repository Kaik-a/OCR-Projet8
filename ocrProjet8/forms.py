from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(label="Sujet", max_length=100)
    email = forms.EmailField(label="E-mail", max_length=100)
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={'cols': 0})
    )

