# Generated by Django 4.0.4 on 2022-04-26 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000)),
                ('datetime', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ArticlePhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='workshop_blog.article')),
            ],
        ),
    ]
