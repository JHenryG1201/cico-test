from django.shortcuts import render

def home(request):
    return render(request, "home.html", {"message": "Hi to your Django App!"})
