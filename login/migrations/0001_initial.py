# Generated by Django 2.0.2 on 2018-02-26 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_login', models.CharField(blank=True, max_length=64, null=True)),
                ('password_login', models.CharField(blank=True, max_length=64, null=True)),
                ('is_active_login', models.BooleanField(default=True)),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('last_name', models.CharField(blank=True, max_length=64, null=True)),
                ('surname', models.CharField(blank=True, max_length=64, null=True)),
                ('session_key_login', models.CharField(blank=True, default=None, max_length=124, null=True)),
                ('updated_login', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Пользователь для входа',
                'verbose_name_plural': 'Пользователи для входа',
            },
        ),
    ]
