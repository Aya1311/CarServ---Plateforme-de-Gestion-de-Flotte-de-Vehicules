# Generated by Django 4.2.1 on 2023-06-17 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pfm", "0027_alter_client_is_user_authenticated_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="client",
            name="last_activity",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="employe",
            name="last_activity",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]