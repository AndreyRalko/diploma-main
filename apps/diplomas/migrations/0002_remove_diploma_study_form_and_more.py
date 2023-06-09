# Generated by Django 4.1.7 on 2023-02-21 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("diplomas", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="diploma",
            name="study_form",
        ),
        migrations.AddField(
            model_name="diploma",
            name="study_form_or_direction",
            field=models.ForeignKey(
                help_text="Форма обучения для бакалавриата, направление для магистратуры",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="diplomas.studyform",
                verbose_name="Форма обучения или направление",
            ),
        ),
        migrations.AlterField(
            model_name="diploma",
            name="is_honors",
            field=models.BooleanField(default=False, verbose_name="Диплом с отличием"),
        ),
    ]
