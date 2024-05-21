from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
  password = forms.CharField(
    label='Password',
    widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
  )
  password2 = forms.CharField(
    label='Confirm Password',
    widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'})
  )

  class Meta:
    model = User
    fields = ["username","first_name", "last_name", "email"]
    widgets = {
      "username" : forms.TextInput(
        attrs={'placeholder' : 'Username'}
      ),
      
      "first_name" : forms.TextInput(
        attrs={'placeholder' : 'First name'}
      ),
      
      "last_name" : forms.TextInput(
        attrs={'placeholder' : 'Last name'}
      ),
      
      "email" : forms.EmailInput(
        attrs={'placeholder' : 'Email address'}
      ),
    }

  def clean_password2(self):
    cd = self.cleaned_data
    if cd['password2'] != cd['password']:
      raise forms.ValidationError("Passwords do not match")
    return cd['password2']
  
  