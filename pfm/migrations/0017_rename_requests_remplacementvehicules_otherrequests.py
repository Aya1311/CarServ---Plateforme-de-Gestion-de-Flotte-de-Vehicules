# Generated by Django 4.2.1 on 2023-06-10 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pfm", "0016_alter_remplacementvehicules_issuetype"),
    ]

    operations = [
        migrations.RenameField(
            model_name="remplacementvehicules",
            old_name="requests",
            new_name="otherrequests",
        ),
    ]
