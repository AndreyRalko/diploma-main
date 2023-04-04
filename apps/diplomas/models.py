from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from simple_history.models import HistoricalRecords

from .services import DiplomaDocument


class StudyForm(models.Model):
    name_kk = models.CharField(verbose_name="Название на казахском", max_length=150)
    name_en = models.CharField(verbose_name="Название на английском", max_length=150)
    name_ru = models.CharField(verbose_name="Название на русском", max_length=150)

    class Meta:
        verbose_name = "Форма обучения (направление магистратуры)"
        verbose_name_plural = "Формы обучения (направления магистратуры)"

    def __str__(self):
        return f"{self.name_kk} - {self.name_en} - {self.name_ru}"


class Specialty(models.Model):
    name_kk = models.CharField(verbose_name="Название на казахском", max_length=150)
    name_en = models.CharField(verbose_name="Название на английском", max_length=150)
    name_ru = models.CharField(verbose_name="Название на русском", max_length=150)
    code = models.CharField(verbose_name="Код специальности", max_length=100)
    is_educational_program = models.BooleanField(
        verbose_name="Образовательная программа",
        default=True,
        help_text="Если True - образовательная программа, иначе - специальность",
    )

    platonus_id = models.IntegerField(
        verbose_name="ID в Platonus", blank=True, null=True
    )

    class Meta:
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"

    def __str__(self):
        return f"{self.code} {self.name_kk}"


class Degree(models.Model):
    name_kk = models.CharField(verbose_name="Название на казахском", max_length=255)
    name_en = models.CharField(verbose_name="Название на английском", max_length=255)
    name_ru = models.CharField(verbose_name="Название на русском", max_length=255)

    class Meta:
        verbose_name = "Степень"
        verbose_name_plural = "Степени"

    def __str__(self):
        return f"{self.name_kk} | {self.name_en} | {self.name_ru}"


class ConferredDegree(models.Model):
    name_kk = models.CharField(verbose_name="Название на казахском", max_length=255)
    name_en = models.CharField(verbose_name="Название на английском", max_length=255)
    name_ru = models.CharField(verbose_name="Название на русском", max_length=255)

    class Meta:
        verbose_name = "Присваемая степень"
        verbose_name_plural = "Присваемые степени"

    def __str__(self):
        return f"{self.name_kk}"


class DiplomaTemplate(models.Model):
    name = models.CharField(
        verbose_name="Название",
        max_length=255,
        help_text="Например: шаблон диплома 2022 года",
    )
    file = models.FileField(verbose_name="Файл шаблона", upload_to="diploma_templates/")

    class Meta:
        verbose_name = "Шаблон диплома"
        verbose_name_plural = "Шаблоны диплома"

    def __str__(self) -> str:
        return self.name


def diploma_directory_path(instance, filename):
    return "diplomas/{0}/{1}".format(instance.iin, filename)


class Diploma(models.Model):
    class DiplomaStatus(models.TextChoices):
        GENERATED = "generated", "Сгенерирован"
        READY_TO_PRINT = "ready", "Готов к печати"
        PRINTED = "printed", "Распечатан"

    template = models.ForeignKey(
        verbose_name="Шаблон диплома",
        to=DiplomaTemplate,
        on_delete=models.PROTECT,
        null=True,
    )
    platonus_id = models.IntegerField(
        verbose_name="ID аккаунта Platonus", null=True, db_index=True
    )
    iin = models.CharField(
        verbose_name="ИИН",
        max_length=30,
        db_index=True,
    )
    firstname_kk = models.CharField(
        verbose_name="Имя на казахском (в дат. падеже)", max_length=255
    )
    lastname_kk = models.CharField(
        verbose_name="Фамилия на казахском (в дат. падеже)", max_length=255
    )
    patronymic_kk = models.CharField(
        verbose_name="Отчество на казахском (в дат. падеже)",
        max_length=255,
        blank=True,
        null=True,
    )
    firstname_en = models.CharField(verbose_name="Имя на английском", max_length=255)
    lastname_en = models.CharField(verbose_name="Фамилия на английском", max_length=255)
    firstname_ru = models.CharField(
        verbose_name="Имя на русском (в дат. падеже)", max_length=255
    )
    lastname_ru = models.CharField(
        verbose_name="Фамилия на русском (в дат. падеже)", max_length=255
    )
    patronymic_ru = models.CharField(
        verbose_name="Отчество на русском (в дат. падеже)",
        max_length=255,
        blank=True,
        null=True,
    )

    study_form_or_direction = models.ForeignKey(
        verbose_name="Форма обучения или направление",
        to=StudyForm,
        on_delete=models.PROTECT,
        help_text="Форма обучения для бакалавриата, направление для магистратуры",
        null=True,
    )
    specialty = models.ForeignKey(
        verbose_name="Специальность / ОП", to=Specialty, on_delete=models.PROTECT
    )
    degree = models.ForeignKey(
        verbose_name="Степень", to=Degree, on_delete=models.PROTECT
    )
    conferred_degree = models.ForeignKey(
        verbose_name="Присваемая степень", to=ConferredDegree, on_delete=models.PROTECT
    )

    # Информация о дипломе
    is_honors = models.BooleanField(verbose_name="Диплом с отличием", default=False)
    protocol_number = models.CharField(verbose_name="Номер протокола", max_length=100)
    protocol_date = models.DateField(
        verbose_name="Дата подписания протокола заседания аттестационной комиссии",
        blank=True,
        null=True,
    )
    diploma_number = models.CharField(
        verbose_name="Серия и номер диплома", max_length=100
    )
    issue_date = models.DateField(
        verbose_name="Дата выдачи диплома", blank=True, null=True
    )
    registration_number = models.CharField(
        verbose_name="Регистрационный номер диплома", max_length=32
    )

    qr = models.FileField(verbose_name="Файл QR", upload_to=diploma_directory_path)
    docx = models.FileField(
        verbose_name="Файл диплома (DOCX)",
        upload_to=diploma_directory_path,
        blank=True,
        null=True,
    )
    pdf = models.FileField(
        verbose_name="Файл диплома (PDF)",
        upload_to=diploma_directory_path,
        blank=True,
        null=True,
    )

    generated_by = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL, blank=True, null=True
    )

    status = models.CharField(
        verbose_name="Статус",
        max_length=32,
        choices=DiplomaStatus.choices,
        default=DiplomaStatus.GENERATED,
    )

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    history = HistoricalRecords()

    class Meta:
        verbose_name = "Диплом"
        verbose_name_plural = "Дипломы"
        constraints = [
            models.UniqueConstraint(
                fields=["iin", "degree", "conferred_degree"], name="iin_degree"
            )
        ]

    def __str__(self):
        return f"<{self.__class__.__name__}> {self.lastname_kk} {self.firstname_kk} - {self.iin}"

    def get_absolute_url(self):
        return reverse("diploma_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        # TODO: generate DOCX and PDF file
        docx = DiplomaDocument(self)
        docx_path = docx.generate_docx()
        self.docx = docx_path
        return super().save(*args, **kwargs)
