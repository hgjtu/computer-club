from django.shortcuts import render
from .forms import UserForm
from .models import MyUser


def user(request):
    form = UserForm(request.GET or None)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, 'users/user.html', context)


def user_profile(request):
    users = MyUser.objects.all()
    context = {'users': users}
    return render(request, 'users/user_profile.html', context)
