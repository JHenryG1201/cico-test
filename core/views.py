from django.shortcuts import render

def home(request):
    return render(request, "home.html", {"message": "Bye to your Django App!"})