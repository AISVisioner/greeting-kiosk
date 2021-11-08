# Generated by Django 3.1.13 on 2021-11-02 12:07

import django.contrib.postgres.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('encoding', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, editable=False), blank=True, size=None)),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('visits_count', models.IntegerField(blank=True, default=1)),
                ('recent_access_at', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
