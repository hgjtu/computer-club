from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.paginator import Paginator
from .forms import UserForm
from .models import MyUser, Session
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
            if (form.cleaned_data['img_path'] is False):
                with open(os.path.join(settings.BASE_DIR,
                                       'media/users/profile_photo/profile.png'), 'rb') as f:
                    form.instance.img_path.save('profile.jpg', File(f))
            form.save()
            return redirect('users:profile', name=name)
    else:
        form = UserForm(instance=instance)
    return render(request, 'users/user_edit.html', {'form': form})


is_filtered = False


@login_required
def user_profile(request, name):
    global is_filtered
    if (not is_filtered):
        instance = get_object_or_404(MyUser, username=name)
        session_id = request.GET.get('session_id', '')
        start_time_from = request.GET.get('start_time_from', '')
        start_time_to = request.GET.get('start_time_to', '')
        end_time_from = request.GET.get('end_time_from', '')
        end_time_to = request.GET.get('end_time_to', '')
        service_name = request.GET.get('servise_id', '')
        equipment_name = request.GET.get('equipment_id', '')

        sessions = Session.objects.filter(user_id=instance).order_by("pk")
        if session_id:
            sessions = sessions.filter(id=session_id)
        if start_time_from:
            sessions = sessions.filter(start_time__gte=start_time_from)
        if start_time_to:
            sessions = sessions.filter(start_time__lte=start_time_to)
        if end_time_from:
            sessions = sessions.filter(end_time__gte=end_time_from)
        if end_time_to:
            sessions = sessions.filter(end_time__lte=end_time_to)
        if service_name:
            sessions = sessions.filter(service_id__title=service_name)
        if equipment_name:
            sessions = sessions.filter(equipment_id__type=equipment_name)

        last_search = sessions
    else:
        sessions = Session.objects.filter(user_id=instance).order_by("pk")

    paginator = Paginator(sessions, 4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'users/user_profile.html',
                  {'view_user': name,
                   'page_obj': page_obj,
                   'last_search': last_search})


@login_required
def fetch_sessions(request):
    user_sessions = Session.objects.filter(user_id=request.user)
    sessions_data = []

    for session in user_sessions:
        sessions_data.append({
            'session_id': session.pk,
            'start_time': session.start_time,
            'end_time': session.end_time,
            'service_id': session.service_id,
            'equipment_id': session.equipment_id,
        })

    return JsonResponse(sessions_data, safe=False)
