# Generated by Django 4.2.4 on 2023-10-10 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_messages_body_alter_messages_user_delete_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-updated', '-created']},
        ),
    ]
