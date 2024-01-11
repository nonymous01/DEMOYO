from django.shortcuts import render, redirect,HttpResponse
from .models import User
# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get("email")
        user = User.objects.create(name=username, email=email)
        user.save()
        return HttpResponse('juste')
    return render(request, 'my_app/index.html')