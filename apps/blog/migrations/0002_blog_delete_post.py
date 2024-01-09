# Generated by Django 5.0 on 2024-01-05 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='название')),
                ('description', models.TextField(max_length=300, verbose_name='описание')),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
