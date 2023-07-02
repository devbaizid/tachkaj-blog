# Generated by Django 4.2.2 on 2023-07-01 16:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_blog_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='thumbnail',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
    ]