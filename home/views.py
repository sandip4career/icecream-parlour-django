from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import contact as Contact
from django.contrib import messages

# Create your views here.

def index(request):

    return render(request, 'index.html')



def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact_entry = Contact(
            name=name,
            email=email,
            message=message,
            date=datetime.today()
        )

        contact_entry.save()
        messages.success(request, "Your message has been sent!!.")

    return render(request, 'contact.html')