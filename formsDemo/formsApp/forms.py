from django import forms
from django.core import validators

class UserRegisterationForm(forms.Form):
    GENDER=[('male','MALE'),('female','FEMALE')]
    firstName=forms.CharField( required=False,validators=[validators.MaxLengthValidator(20),validators.MinLengthValidator(5)])
    lastName=forms.CharField()
    email=forms.EmailField()
    gender = forms.CharField(widget=forms.Select(choices=GENDER))
    password = forms.CharField(widget=forms.PasswordInput)
    ssn = forms.IntegerField() 


'''
    #custom validations single function
    def clean(self):
        user_cleaned_data = super().clean()
        inputFirstName = user_cleaned_data['firstName']
        if len(inputFirstName)>20:
            raise forms.ValidationError('max length exceeded')

        inputEmail = user_cleaned_data['email']
        if inputEmail.find('@')==-1:
            raise forms.ValidationError('invalid email')
        return inputEmail


    #custom validations individual functions
    def clean_firstName(self):
        inputFirstName = self.cleaned_data['firstName']
        if len(inputFirstName)>20:
            raise forms.ValidationError('max length exceeded')
        return inputFirstName

    def clean_email(self):
        inputEmail = self.cleaned_data['email']
        if inputEmail.find('@')==-1:
            raise forms.ValidationError('invalid email')
        return inputEmail

'''