from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from .models import MyUser


def success_registration(request):
    return render(request, 'registration/great_success.html')


@login_required
def user_edit(request, name):
    instance = get_object_or_404(MyUser, username=name)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('users:profile', name=name)
    else:
        form = UserForm(instance=instance)   
    return render(request, 'users/user_edit.html', {'form': form})


@login_required
def user_profile(request, name):
    # instance = get_object_or_404(MyUser, username=name)
    return render(request, 'users/user_profile.html', {'view_user': name})
