from django.shortcuts import render

def home(request):
    return render(request, "home.html", {"message": "Hi Hi to your Django App!"})
