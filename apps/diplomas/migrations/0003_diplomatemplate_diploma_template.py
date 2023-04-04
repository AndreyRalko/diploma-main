# Generated by Django 4.1.7 on 2023-02-23 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("diplomas", "0002_remove_diploma_study_form_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="DiplomaTemplate",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Например: шаблон диплома 2022 года",
                        max_length=255,
                        verbose_name="Название",
                    ),
                ),
                (
                    "file",
                    models.FileField(
                        upload_to="diploma_templates/", verbose_name="Файл шаблона"
                    ),
                ),
            ],
            options={
                "verbose_name": "Шаблон диплома",
                "verbose_name_plural": "Шаблоны диплома",
            },
        ),
        migrations.AddField(
            model_name="diploma",
            name="template",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="diplomas.diplomatemplate",
                verbose_name="Шаблон диплома",
            ),
        ),
    ]
