# Generated by Django 2.2.9 on 2020-01-25 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testruns', '0007_migration_due_to_add_related_name_to_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testrun',
            name='errata_id',
        ),
    ]
