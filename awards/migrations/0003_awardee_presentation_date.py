# Generated by Django 3.0.7 on 2020-06-20 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0002_auto_20200620_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='awardee',
            name='presentation_date',
            field=models.DateField(null=True),
        ),
    ]