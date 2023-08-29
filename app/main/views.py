from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'client/index.html')

def apropos(request):
    return render(request, 'client/about.html')

def service(request):
    return render(request, 'client/services.html')

def client(request):
    return render(request, 'client/client.html')

def contact(request):
    return render(request, 'client/contact.html')