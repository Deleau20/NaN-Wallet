from NaN_Wallet import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

# Create your views here.


@csrf_protect
def register(request):
    if request.method == "POST":
        try:
            username = request.POST['username']
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            email = request.POST['email']
            password = request.POST['password']
            password_confirm = request.POST['password_confirm']
            
            if User.objects.filter(username=username).exists():
                messages.error(request, "Les informations entrées sont invalides.") 
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.error(request, "Les informations entrées sont invalides.")
                return redirect('register')
            if not username.isalnum():
                messages.error(request, "Le nom d'utilisateur ne doit contenir que des lettres et des chiffres.")
                return redirect('register')
            
            if password != password_confirm:
                messages.error(request, "Les mots de passe ne correspondent pas.")
                return redirect('register')
            
            print("Utilisateur créé avec succès !")
            utilisateur = User.objects.create_user(username, email, password)
            print("Utilisateur créé avec succès ! &&&&&&&&&&&")
            utilisateur.first_name = firstname
            utilisateur.last_name = lastname
            utilisateur.save()
            return render(request, 'authentification/login.html')
        
        except Exception as e:
            # Gérez l'exception ici, par exemple, en affichant un message d'erreur générique.
            messages.error(request, "Une erreur s'est produite lors de l'inscription.")
            print(f"Erreur lors de l'inscription : {str(e)}")
            return redirect('register')
    
    return render(request, 'authentification/register.html')

@csrf_protect
def login(request):
    if request.method == "POST":
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth_login(request, user)
                first_name = request.user.first_name
                return render(request, 'dashClient/confirmation.html')
            else:
                messages.error(request, "Identifiants invalides.")
                return redirect('login')
        
        except Exception as e:
            # Gérez l'exception ici, par exemple, en affichant un message d'erreur générique.
            messages.error(request, "Une erreur s'est produite lors de la connexion.")
            print(f"Erreur lors de la connexion : {str(e)}")
            return redirect('login')
    
    return render(request, 'authentification/login.html')


def logOut(request):
    logout(request)
    messages.success(request, "Vous avez été déconnecté avec succès !")
    return redirect('home')

def forgot_pwd(request):
    return render(request, 'authentification/forgot-pwd.html')