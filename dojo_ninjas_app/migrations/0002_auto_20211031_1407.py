# Generated by Django 2.2 on 2021-10-31 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ninjas',
            old_name='last_city',
            new_name='last_name',
        ),
    ]