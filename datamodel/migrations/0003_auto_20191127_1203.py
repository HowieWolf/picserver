# Generated by Django 2.2.7 on 2019-11-27 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamodel', '0002_auto_20191127_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appeal',
            name='time_apply',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='copyright',
            name='img',
            field=models.ImageField(upload_to='static/copyright/%y/%m/%d'),
        ),
    ]
