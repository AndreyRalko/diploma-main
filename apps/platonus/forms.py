from dal import autocomplete
from django import forms

from .models import Student


class StudentSearchForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("iin",)

        widgets = {
            "iin": autocomplete.ListSelect2(
                url="student_autocomplete", attrs={"required": True}
            ),
        }

        labels = {
            "iin": "ИИН для поиска",
        }
