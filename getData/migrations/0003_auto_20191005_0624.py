# Generated by Django 2.2.5 on 2019-10-05 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getData', '0002_auto_20191005_0623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phoneuser',
            name='otp',
            field=models.IntegerField(default=79517),
        ),
    ]
