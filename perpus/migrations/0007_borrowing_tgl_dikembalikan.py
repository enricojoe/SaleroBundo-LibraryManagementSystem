# Generated by Django 2.2.10 on 2021-05-25 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perpus', '0006_auto_20210525_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowing',
            name='tgl_dikembalikan',
            field=models.DateTimeField(null=True),
        ),
    ]
