# Generated by Django 2.0.2 on 2018-03-05 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20180305_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_project',
            name='pair',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='sub_project_prime_data',
            name='key_yacor_project',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]