# Generated by Django 4.2.1 on 2023-06-12 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pfm", "0024_vechule_cas"),
    ]

    operations = [
        migrations.AddField(
            model_name="remplacementvechule",
            name="historique",
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
