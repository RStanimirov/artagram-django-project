# Generated by Django 3.2.15 on 2022-11-13 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_artwork'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='artwork',
            field=models.ImageField(default='default-artwork.png', upload_to='artworks'),
        ),
    ]
