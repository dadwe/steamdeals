from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from listapp.models import Steam, Steam_g2a, Humble, HumbleG2a, Feedback
from django.views.generic import TemplateView
from listapp.forms import FeedbackForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def other_index(request):
    return render(request, "listapp/landing.html")


def home_index(request):
    return render(request, "listapp/home.html")


def login_index(request):
    return render(request, "listapp/login.html")

def logout_index(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/login')

# @login_required(login_url="/login")
def steamsales_index(request):
    sales = Steam.objects.all()
    g2a_steam = Steam_g2a.objects.all()

    paginator = Paginator(g2a_steam, 25)
    page = request.GET.get('page')
    g2a_steam = paginator.get_page(page)
    return render(request, "listapp/steamsales.html", {'sales': sales,
                                                       'g2a_steam': g2a_steam})

# @login_required(login_url="/login")
def humblesales_index(request):
    sales = Humble.objects.all()
    g2a_humble = HumbleG2a.objects.order_by('margin_percent').reverse()  # reverse() for largest to smallest
    paginator = Paginator(g2a_humble, 25)
    page = request.GET.get('page')
    g2a_humble = paginator.get_page(page)
    return render(request, "listapp/humblesales.html", {'sales': sales,
                                                        'g2a_humble': g2a_humble})

# @login_required(login_url="/login")
def feedback_index(request):
    form = FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedbackField = request.POST.get('feedback','')
            feedbackObj = Feedback(feedback=feedbackField)
            feedbackObj.save()
            return redirect('/thanks')

    return render(request, "listapp/feedback.html", {'form':form})

def thanks_index(request):
    return render(request, 'listapp/thanks.html')
