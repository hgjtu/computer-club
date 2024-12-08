from django.shortcuts import render, get_object_or_404
from .forms import UserForm
from .models import MyUser


def success_registration(request):
    return render(request, 'registration/great_success.html')


def user_edit(request, name):
    instance = get_object_or_404(MyUser, username=name)
    form = UserForm(request.GET or None, instance=instance)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, 'users/user_edit.html', context)


def user_profile(request):
    users = MyUser.objects.all()
    context = {'users': users}
    return render(request, 'users/user_profile.html', context)
