# Generated by Django 4.1.7 on 2023-02-23 08:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("diplomas", "0003_diplomatemplate_diploma_template"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="studyform",
            options={
                "verbose_name": "Форма обучения (направление магистратуры)",
                "verbose_name_plural": "Формы обучения (направления магистратуры)",
            },
        ),
    ]