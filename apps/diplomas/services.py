from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .models import Diploma

from datetime import datetime

from docxtpl import DocxTemplate

from .consts import MONTHS, MONTHS_WITH_ENDING


class DiplomaDocument:
    def __init__(self, data: "Diploma") -> None:
        self.data = data

    def generate_docx(self) -> str:
        docx = DocxTemplate(self.data.template.file.path)

        docx.replace_pic("qr_code", self.data.qr)
        docx.render(self.__get_context())

        date = datetime.now().strftime("%Y_%m_%d-%I %M %S")

        file_path = "diplomas/{}/{} {} - {}_{}.docx".format(
            self.data.iin,
            self.data.lastname_kk,
            self.data.firstname_kk,
            self.data.diploma_number,
            date,
        )

        docx.save("media/" + file_path)

        return file_path

    def __get_context(self) -> dict:
        context = {
            "di_number": self.data.diploma_number,
            "p_year": self.data.protocol_date.year,
            "p_day": self.data.protocol_date.day,
            "p_month_kk": MONTHS_WITH_ENDING[self.data.protocol_date.month][
                "name_kk"
            ].lower(),
            "p_month_en": MONTHS_WITH_ENDING[self.data.protocol_date.month]["name_en"],
            "p_month_ru": MONTHS_WITH_ENDING[self.data.protocol_date.month][
                "name_ru"
            ].lower(),
            "p_number": self.data.protocol_number,
            "fname_kk": self.data.firstname_kk,
            "fname_en": self.data.firstname_en,
            "fname_ru": self.data.firstname_ru,
            "lname_kk": self.data.lastname_kk,
            "lname_en": self.data.lastname_en,
            "lname_ru": self.data.lastname_ru,
            "patronymic_kk": self.data.patronymic_kk or "",
            "patronymic_ru": self.data.patronymic_ru or "",
            "s_code": self.data.specialty.code,
            "s_name_kk": self.data.specialty.name_kk,
            "s_name_en": self.data.specialty.name_en,
            "s_name_ru": self.data.specialty.name_ru,
            "s_form_kk": self.data.study_form_or_direction.name_kk.lower(),
            "s_form_en": self.data.study_form_or_direction.name_en.lower(),
            "s_form_ru": self.data.study_form_or_direction.name_ru.lower(),
            "reg_number": self.data.registration_number.replace(" ", ""),
            "iss_y": self.data.issue_date.year,
            "iss_d": self.data.issue_date.day,
            "iss_m_kk": MONTHS[self.data.issue_date.month]["name_kk"].lower(),
            "iss_m_en": MONTHS[self.data.issue_date.month]["name_en"],
            "iss_m_ru": MONTHS_WITH_ENDING[self.data.issue_date.month][
                "name_ru"
            ].lower(),
            "degree_kk": self.data.degree.name_kk.upper(),
            "degree_en": self.data.degree.name_en.upper(),
            "degree_ru": self.data.degree.name_ru.upper(),
            "conferred_degree_kk": self.data.conferred_degree.name_kk,
            "conferred_degree_en": self.data.conferred_degree.name_en,
            "conferred_degree_ru": self.data.conferred_degree.name_ru,
        }

        if "магистр" in self.data.degree.name_ru.lower():
            # в дипломе магистра вместо "форма обучения" идет "направление"
            # (научно-педагогическое и тд)
            context["st_dir_kk"] = "Бағыты"
            context["st_dir_en"] = "Type of program"
            context["st_dir_ru"] = "Направление"
        else:
            context["st_dir_kk"] = "Оқыту нысаны"
            context["st_dir_en"] = "Form of study"
            context["st_dir_ru"] = "Форма обучения"

        if self.data.specialty.is_educational_program:
            context["edu_program_text_ru"] = "по образовательной программе"
            context["edu_program_text_kk"] = "білім беру бағдарламасы бойынша"
        else:
            context["edu_program_text_ru"] = "по специальности"
            context["edu_program_text_kk"] = "мамандығы бойынша"

        return context
