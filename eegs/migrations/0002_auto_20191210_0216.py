# Generated by Django 2.1.5 on 2019-12-10 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eegs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trial',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
