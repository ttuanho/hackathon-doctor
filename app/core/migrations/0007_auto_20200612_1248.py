# Generated by Django 3.0.7 on 2020-06-12 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200612_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profession',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='registration_expiry_date',
            field=models.DateTimeField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='registration_number',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
