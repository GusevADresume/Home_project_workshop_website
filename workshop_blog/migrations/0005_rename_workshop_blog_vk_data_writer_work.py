# Generated by Django 4.0.4 on 2022-04-30 23:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workshop_blog', '0004_vk_data_workshop_blog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vk_data',
            old_name='workshop_blog',
            new_name='writer_work',
        ),
    ]