# Generated by Django 2.2.3 on 2019-07-12 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_auto_20190712_0733'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.TextField(default='ashlam'),
        ),
    ]