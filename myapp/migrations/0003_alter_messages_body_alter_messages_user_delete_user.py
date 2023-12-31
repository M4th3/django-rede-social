# Generated by Django 4.2.4 on 2023-10-06 15:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0002_topic_user_room_host_messages_room_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='body',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='messages',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
