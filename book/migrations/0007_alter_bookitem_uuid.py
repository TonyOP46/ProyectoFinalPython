# Generated by Django 3.2 on 2022-05-29 07:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_alter_bookitem_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookitem',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('5df39ebb-f202-4a49-8eb9-afc394553fda'), editable=False),
        ),
    ]
