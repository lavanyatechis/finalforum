# Generated by Django 3.2.6 on 2021-08-11 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.CharField(blank=True, db_index=True, max_length=140, null=True, verbose_name='Body'),
        ),
    ]
