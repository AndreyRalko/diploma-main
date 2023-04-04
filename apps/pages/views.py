from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView

from apps.platonus.forms import StudentSearchForm


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["form"] = StudentSearchForm()

        return context

    def post(self, request, *args, **kwargs):
        student_id = 0

        try:
            student_id = request.POST["iin"]
        except:
            pass

        return redirect(reverse("diploma_create") + f"?student_id={student_id}")


class AboutPageView(TemplateView):
    template_name = "pages/about.html"
