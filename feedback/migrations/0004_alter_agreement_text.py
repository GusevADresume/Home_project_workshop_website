# Generated by Django 4.0.4 on 2022-04-27 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_agreement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agreement',
            name='text',
            field=models.TextField(max_length=10000),
        ),
    ]
