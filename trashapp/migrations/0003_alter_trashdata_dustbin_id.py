# Generated by Django 4.2.5 on 2023-09-26 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trashapp', '0002_alter_trashdata_dustbin_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trashdata',
            name='dustbin_id',
            field=models.CharField(max_length=10, null=True),
        ),
    ]