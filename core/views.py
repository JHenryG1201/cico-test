from django.shortcuts import render

def home(request):
    return render(request, "home.html", {"message": "Bye Bye to your Django App!"})
