# Generated by Django 4.2.1 on 2023-05-21 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("pfm", "0002_customuser"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="custom_groups",
            field=models.ManyToManyField(
                related_name="custom_user_groups", to="auth.group"
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="custom_user_permissions",
            field=models.ManyToManyField(
                related_name="custom_user_permissions", to="auth.permission"
            ),
        ),
    ]
