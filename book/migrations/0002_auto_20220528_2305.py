# Generated by Django 3.2 on 2022-05-29 04:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookitem',
            name='rent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rent', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bookitem',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('e9384585-c8e0-4132-9018-103b022380e0'), editable=False),
        ),
    ]
