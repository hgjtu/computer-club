from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from .models import MyUser
from django.conf import settings

import os
from django.core.files import File


def success_registration(request):
    return render(request, 'registration/great_success.html')


@login_required
def user_edit(request, name):
    instance = get_object_or_404(MyUser, username=name)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            print(form.cleaned_data)
            if (form.cleaned_data['img_path'] is False):
                with open(os.path.join(settings.BASE_DIR,
                          'media/users/profile_photo/profile.png'), 'rb') as f:
                    form.instance.img_path.save('profile.jpg', File(f))
            form.save()
            return redirect('users:profile', name=name)
    else:
        form = UserForm(instance=instance)
    return render(request, 'users/user_edit.html', {'form': form})


@login_required
def user_profile(request, name):
    # instance = get_object_or_404(MyUser, username=name)
    return render(request, 'users/user_profile.html', {'view_user': name})
