from django.shortcuts import render
from . import forms

# Create your views here.
def userRegisterationView(request):
    form=forms.UserRegisterationForm()
    if request.method == 'POST':
        form= forms.UserRegisterationForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            print("Firstname", form.cleaned_data['firstName'])
            print("lastname", form.cleaned_data['lastName'])
            print("email", form.cleaned_data['email'])
    return render(request,'formDemo/userRegisteration.html',{'form':form})