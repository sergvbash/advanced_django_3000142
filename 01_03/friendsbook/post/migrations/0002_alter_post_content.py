# Generated by Django 4.1.2 on 2022-10-20 20:47

from django.db import migrations, models
import post.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(max_length=140, validators=[post.models.validade_no_bad_words]),
        ),
    ]
