# Generated by Django 4.2.1 on 2023-06-11 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("pfm", "0020_remplacement_delete_remplacementvehicules"),
    ]

    operations = [
        migrations.CreateModel(
            name="Remplacementvechule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("issuetype", models.CharField(blank=True, max_length=50, null=True)),
                ("gam", models.CharField(blank=True, max_length=40, null=True)),
                ("status", models.CharField(blank=True, max_length=40, null=True)),
                ("date", models.DateField(blank=True, null=True)),
                (
                    "otherrequests",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("dateincident", models.DateField(blank=True, null=True)),
                (
                    "lieu_incident",
                    models.CharField(blank=True, max_length=40, null=True),
                ),
                (
                    "Description",
                    models.CharField(blank=True, max_length=1000000000000, null=True),
                ),
                (
                    "type_de_reparation",
                    models.CharField(blank=True, max_length=40, null=True),
                ),
                ("date_envoi", models.DateTimeField(auto_now_add=True)),
                (
                    "client",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="pfm.client",
                    ),
                ),
                (
                    "vechule",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="pfm.vechule",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(name="Remplacement",),
    ]