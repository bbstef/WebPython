# Generated by Django 2.2.2 on 2019-06-03 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
