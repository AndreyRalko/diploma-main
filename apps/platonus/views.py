from dal import autocomplete
from django.db.models import Q
from django.utils.html import format_html

from .models import Student


class StudentAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Student.objects.using("platonus").none()

        qs = Student.objects.using("platonus").all().select_related("study_form")

        if self.q:
            qs = qs.filter(iin__icontains=self.q)

        return qs

    def get_result_label(self, result):
        return format_html(
            "{} {} {} ({}) - дата поступления {}",
            result.lastname,
            result.firstname,
            result.patronymic,
            result.study_form.name_ru,
            result.startdate,
        )
