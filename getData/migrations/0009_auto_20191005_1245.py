# Generated by Django 2.2.5 on 2019-10-05 07:15

from django.db import migrations, models
import getData.models


class Migration(migrations.Migration):

    dependencies = [
        ('getData', '0008_auto_20191005_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phoneuser',
            name='otp',
            field=models.IntegerField(default=52911),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, max_length=254, null=True, upload_to=getData.models.nameFile),
        ),
    ]
