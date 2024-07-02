# Generated by Django 5.0.6 on 2024-07-02 11:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_alter_modelo_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="Veiculo",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("ano", models.IntegerField()),
                ("preco", models.DecimalField(decimal_places=2, max_digits=10)),
                ("acessorios", models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to="core.acessorio")),
                ("cor", models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to="core.cor")),
                ("modelo", models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to="core.modelo")),
            ],
            options={
                "verbose_name": "Veículo",
                "verbose_name_plural": "Veículos",
            },
        ),
    ]
