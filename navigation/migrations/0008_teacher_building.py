# Generated by Django 4.1.13 on 2024-03-09 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0007_teacher_floor'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='building',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='navigation.building'),
        ),
    ]
