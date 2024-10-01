from  django import forms


class studentRegistration(forms.Form):
     stuid = forms.IntegerField()
     name = forms.CharField(help_text="make it 100 characters")
     email = forms.EmailField()
     password = forms.CharField(widget=forms.PasswordInput)     