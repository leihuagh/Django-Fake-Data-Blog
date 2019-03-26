from django import forms


class ContactForm(forms.Form):
    fullname = forms.CharField(
        label="Full Name",
        widget=forms.TextInput(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "Your full name"
            }
        )
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "Your email demo@example.com"
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "Content",
                "rows": "4",
            }
        )
    )
