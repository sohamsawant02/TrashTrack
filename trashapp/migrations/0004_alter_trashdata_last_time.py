# Generated by Django 4.2.5 on 2023-09-26 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trashapp', '0003_alter_trashdata_dustbin_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trashdata',
            name='last_time',
            field=models.DateTimeField(null=True),
        ),
    ]
