# Generated by Django 2.1.4 on 2018-12-16 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodelname',
            name='my_field_name',
            field=models.CharField(help_text='Enter field documentation', max_length=50),
        ),
    ]