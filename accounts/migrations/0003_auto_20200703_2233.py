# Generated by Django 3.0.7 on 2020-07-04 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200703_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='rank',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='unit',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
