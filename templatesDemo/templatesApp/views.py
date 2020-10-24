from django.shortcuts import render

# Create your views here.
def renderTemplate(request):
    myDict={'name':'Adnan'}
    return render(request,'templatesApp/firstTemplate.html',myDict)

def renderEmployee(request):
    myDict={'id':123,'name':'Adnan','salary':879546213}
    return render(request,'templatesApp/employeeData.html',myDict)
