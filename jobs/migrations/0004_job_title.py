# Generated by Django 3.1.7 on 2021-03-04 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20210303_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='title',
            field=models.CharField(default='obj', max_length=50),
            preserve_default=False,
        ),
    ]
