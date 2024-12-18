# Generated by Django 5.1.4 on 2024-12-05 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('age', models.IntegerField(default=0, verbose_name='Возраст')),
                ('description', models.CharField(max_length=50, verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Работники',
                'verbose_name_plural': 'Работники',
            },
        ),
        migrations.CreateModel(
            name='Table2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('range', models.CharField(max_length=50, verbose_name='Звание')),
                ('age', models.IntegerField(default=0, verbose_name='Возраст')),
                ('qualification', models.CharField(max_length=50, verbose_name='квалификация')),
            ],
            options={
                'verbose_name': 'Специалисты',
                'verbose_name_plural': 'Специалисты',
            },
        ),
    ]
