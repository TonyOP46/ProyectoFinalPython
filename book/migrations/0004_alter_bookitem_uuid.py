# Generated by Django 3.2 on 2022-05-29 06:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20220529_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookitem',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('859c2b6e-c5df-4d47-abf7-49a5e78cbf14'), editable=False),
        ),
    ]
