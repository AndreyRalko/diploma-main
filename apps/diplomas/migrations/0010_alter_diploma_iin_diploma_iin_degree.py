# Generated by Django 4.1.7 on 2023-03-10 11:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("diplomas", "0009_diploma_status_historicaldiploma_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="diploma",
            name="iin",
            field=models.CharField(db_index=True, max_length=30, verbose_name="ИИН"),
        ),
        migrations.AddConstraint(
            model_name="diploma",
            constraint=models.UniqueConstraint(
                fields=("iin", "degree", "conferred_degree"), name="iin_degree"
            ),
        ),
    ]
