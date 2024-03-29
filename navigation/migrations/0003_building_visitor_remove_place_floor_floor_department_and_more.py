# Generated by Django 4.1.13 on 2024-03-07 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0002_place_title_alter_teacher_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=255)),
                ('reason', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='place',
            name='floor',
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('svg', models.TextField(blank=True, null=True)),
                ('building', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='navigation.building')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('building', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='navigation.building')),
                ('floor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='navigation.floor')),
            ],
        ),
        migrations.AddField(
            model_name='place',
            name='floor_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='navigation.floor'),
        ),
    ]
