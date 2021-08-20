from django.shortcuts import render
from users.models import User


# Create your views here.

def home_screen_view(request):
    context = {}

    users = User.objects.all()

    context['users'] = users

    return render(request, "homeapp/home.html", context)
