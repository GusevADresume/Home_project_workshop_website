# Generated by Django 4.0.4 on 2022-04-30 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop_blog', '0003_vk_data_alter_articlephoto_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='vk_data',
            name='workshop_blog',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
