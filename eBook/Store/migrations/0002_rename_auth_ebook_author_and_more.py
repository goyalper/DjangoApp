# Generated by Django 4.0.1 on 2022-01-06 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ebook',
            old_name='Auth',
            new_name='Author',
        ),
        migrations.RenameField(
            model_name='ebook',
            old_name='cvr_img',
            new_name='cover_image',
        ),
    ]