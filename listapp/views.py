from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from listapp.models import Steam, Steam_g2a


def other_index(request):
    return render(request, "listapp/landing.html")


@login_required(login_url="/login")
def home_index(request):
    return render(request, "listapp/home.html")


def login_index(request):
    return render(request, "listapp/login.html")

def logout_index(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/login')

@login_required(login_url="/login")
def steamsales_index(request):
    sales = Steam.objects.all()
    g2a_steam = Steam_g2a.objects.all()
    current_user = request.user
    return render(request, "listapp/steamsales.html", {'sales': sales,
                                                       'g2a_steam': g2a_steam})
