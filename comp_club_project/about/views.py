from django.shortcuts import render

from django.views.generic import TemplateView
from users.models import MyUser

# from contest.models import Contest


class Description(TemplateView):
    template_name = "about/description.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_count"] = MyUser.objects.count()
        return context
