# Generated by Django 2.2.3 on 2019-07-13 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0004_product_sample_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sample_image',
            field=models.ImageField(blank=True, null=True, upload_to='Photo%Y/%m/%D/'),
        ),
    ]
