from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=15)
    password = forms.CharField(max_length=15, widget=forms.PasswordInput)


class PostMessageForm(forms.Form):
    name = forms.CharField(max_length=15, required=False)
    message = forms.CharField(widget=forms.widgets.Textarea())
    upload_file = forms.FileField(required=False)
