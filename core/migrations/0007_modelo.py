# Generated by Django 5.0.6 on 2024-07-02 11:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_alter_marca_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="Modelo",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("categoria", models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to="core.categoria")),
                ("marca", models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to="core.marca")),
            ],
        ),
    ]