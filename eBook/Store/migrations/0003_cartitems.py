# Generated by Django 4.0.1 on 2022-01-16 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0002_rename_auth_ebook_author_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]