from django.shortcuts import render

# Create your views here.
def electronics(request):
    productDict={'prod1':'Mac','prod2':'Mac','prod3':'Mac'}
    return render(request,'productApp/products.html',productDict)

def toys(request):
    productDict={'prod1':'remote car','prod2':'drone','prod3':'launcher'}
    return render(request,'productApp/products.html',productDict)

def shoes(request):
    productDict={'prod1':'addidas','prod2':'nike','prod3':'reebok'}
    return render(request,'productApp/products.html',productDict)

def index(request):
    return render(request,'productApp/index.html')
