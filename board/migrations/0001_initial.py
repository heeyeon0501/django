# Generated by Django 2.1.5 on 2019-01-15 07:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=datetime.datetime(2019, 1, 15, 7, 0, 18, 552419, tzinfo=utc))),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
