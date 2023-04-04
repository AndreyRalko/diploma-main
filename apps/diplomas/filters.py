import django_filters
from dal import autocomplete
from django.db.models import Q

from .models import Diploma, Specialty


class DiplomaFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(method="search_by_name", label="ФИО")
    specialty = django_filters.ModelChoiceFilter(
        queryset=Specialty.objects.all(),
        widget=autocomplete.ModelSelect2(url="specialty_autocomplete"),
    )

    class Meta:
        model = Diploma
        fields = ["name", "degree", "specialty", "is_honors", "status"]

    def search_by_name(self, queryset, name, value):
        return self.queryset.filter(
            Q(
                firstname_kk__icontains=value,
            )
            | Q(lastname_kk__icontains=value)
            | Q(patronymic_kk__icontains=value)
            | Q(
                firstname_en__icontains=value,
            )
            | Q(lastname_en__icontains=value)
            | Q(
                firstname_ru__icontains=value,
            )
            | Q(lastname_ru__icontains=value)
            | Q(patronymic_ru__icontains=value)
        )


class DiplomaAdminFilter(DiplomaFilter):
    class Meta:
        model = Diploma
        fields = ["name", "degree", "specialty", "is_honors", "status", "generated_by"]
