# Generated by Django 3.1.1 on 2022-05-05 13:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, validators=[django.core.validators.MaxLengthValidator(50), django.core.validators.MinLengthValidator(8)])),
                ('Position', models.CharField(max_length=50)),
                ('Office', models.CharField(max_length=50)),
                ('Age', models.IntegerField(validators=[django.core.validators.MinValueValidator(13)])),
            ],
        ),
    ]
