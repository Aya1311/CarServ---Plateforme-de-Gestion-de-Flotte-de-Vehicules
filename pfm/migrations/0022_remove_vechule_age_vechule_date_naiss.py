# Generated by Django 4.2.1 on 2023-06-11 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pfm", "0021_remplacementvechule_delete_remplacement"),
    ]

    operations = [
        migrations.RemoveField(model_name="vechule", name="age",),
        migrations.AddField(
            model_name="vechule",
            name="date_naiss",
            field=models.DateField(blank=True, max_length=10, null=True),
        ),
    ]
