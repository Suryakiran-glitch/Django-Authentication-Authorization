# Generated by Django 3.1.6 on 2021-02-09 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210209_0340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='permissions',
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='role',
            field=models.CharField(default='subscriber', max_length=50),
        ),
        migrations.DeleteModel(
            name='Permission',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]