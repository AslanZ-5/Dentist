# Generated by Django 3.1.5 on 2021-01-25 12:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210124_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 25, 15, 36, 21, 692066)),
        ),
    ]
