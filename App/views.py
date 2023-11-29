from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.contrib import messages

from. models import Client, Trip

# Create your views here.

def index(request):
    context = {'link' : 'index'}
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html', {'link' : 'contact'})

def service(request):
    return render(request, 'services.html')

def  about(request):
    return render(request, 'about.html')

def  cars(request):
    return render(request, 'cars.html')

def  blog(request):
    return render(request, 'blog.html')


def enterdetails(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        message = request.POST.get('message')

        client = Client(fname =fname, lname=lname, email=email, message=message)
        client.save()
        messages.success(request, 'Successfully Saved!')
        return redirect('/contact')



    return redirect('/contact')
