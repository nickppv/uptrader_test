# Generated by Django 5.0.4 on 2024-04-10 11:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('just_menu', '0004_rename_levelone_first_rename_leveltwo_second_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='third',
            name='level_two',
        ),
        migrations.RenameModel(
            old_name='First',
            new_name='Country',
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('second_level', models.TextField(max_length=30, verbose_name='Производитель')),
                ('level_one', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brand', to='just_menu.country')),
            ],
            options={
                'verbose_name': 'Производитель',
                'verbose_name_plural': 'Производители',
            },
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('third_level', models.TextField(max_length=30, verbose_name='Модель')),
                ('level_two', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='model', to='just_menu.brand')),
            ],
            options={
                'verbose_name': 'Модель',
                'verbose_name_plural': 'Модели',
            },
        ),
        migrations.DeleteModel(
            name='Second',
        ),
        migrations.DeleteModel(
            name='Third',
        ),
    ]