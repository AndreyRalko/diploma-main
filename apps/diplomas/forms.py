from dal import autocomplete
from django import forms

from .models import Diploma


class DiplomaForm(forms.ModelForm):
    protocol_date = forms.DateField(
        label="Дата подписания протокола заседания аттестационной комиссии",
        widget=forms.TextInput(attrs={"type": "date"}),
    )
    issue_date = forms.DateField(
        label="Дата выдачи диплома",
        widget=forms.TextInput(attrs={"type": "date"}),
    )
    platonus_id = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Diploma
        fields = (
            "template",
            "platonus_id",
            "iin",
            "firstname_kk",
            "lastname_kk",
            "patronymic_kk",
            "firstname_en",
            "lastname_en",
            "firstname_ru",
            "lastname_ru",
            "patronymic_ru",
            "study_form_or_direction",
            "specialty",
            "conferred_degree",
            "degree",
            "is_honors",
            "protocol_number",
            "protocol_date",
            "diploma_number",
            "issue_date",
            "registration_number",
            "qr",
        )

        widgets = {
            "specialty": autocomplete.ModelSelect2(url="specialty_autocomplete"),
            "conferred_degree": autocomplete.ModelSelect2(
                url="conferred_degree_autocomplete"
            ),
        }

        labels = {
            "degree": "",
        }


class DiplomaStatusForm(forms.ModelForm):
    class Meta:
        model = Diploma
        fields = ("status",)
