# Generated by Django 2.2.2 on 2019-06-19 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20190619_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.AutoField(help_text='Generate unique ID for Books', primary_key=True, serialize=False),
        ),
    ]
