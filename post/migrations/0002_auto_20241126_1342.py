# Generated by Django 3.1.14 on 2024-11-26 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img_link',
            field=models.TextField(),
        ),
    ]
