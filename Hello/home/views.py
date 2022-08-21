from django.http import HttpRequest
from django.shortcuts import render 
from datetime import datetime
from home.models import contact
from django.contrib.messages import constants as messages

# Create your views here.
def index(request):
    # return HttpResponse('This is home page')
    # context={
    #     'variable':'this is sent'
    # }
    return render(request,'home/index.html')
def about(request):
    return render(request,'home/about.html')

def product(request):
    return render(request,'home/product.html')
        
def contact(request):
    if request.method=='Post':
        name=request.POST.get('name')
        email=request.POST.get('email')
        description=request.POST.get('description')
        Contact=contact(name=name, email=email, description=description, date=datetime.today())
        Contact.save()
        messages.success(request, 'Your form submitted. Thanks for visisting!')
    return render(request,'home/contact.html')
    

    