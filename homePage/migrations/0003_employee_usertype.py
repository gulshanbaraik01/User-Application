# Generated by Django 2.2.2 on 2020-01-25 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0002_auto_20200125_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='usertype',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
