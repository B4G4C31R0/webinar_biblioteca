# Generated by Django 3.2.4 on 2021-06-22 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teste',
            name='nome',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
