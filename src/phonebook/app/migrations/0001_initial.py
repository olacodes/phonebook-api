# Generated by Django 2.2.7 on 2019-11-08 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phonebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastname', models.CharField(max_length=255, unique=True)),
                ('firstname', models.CharField(max_length=255, unique=True)),
                ('phone_number', models.CharField(default='000000000', max_length=25)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.TextField(max_length=255)),
            ],
        ),
    ]