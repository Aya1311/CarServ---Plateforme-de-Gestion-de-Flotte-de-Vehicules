# Generated by Django 4.2.1 on 2023-06-05 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pfm", "0009_vechule"),
    ]

    operations = [
        migrations.AddField(
            model_name="client",
            name="gender",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="employe",
            name="gender",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]