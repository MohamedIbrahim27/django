# Generated by Django 4.1.1 on 2022-10-03 14:11

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_project_detail_image1'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_detail',
            name='image2',
            field=models.ImageField(blank=True, upload_to=main.models.image_upload_detail2),
        ),
        migrations.AddField(
            model_name='project_detail',
            name='image3',
            field=models.ImageField(blank=True, upload_to=main.models.image_upload_detail3),
        ),
        migrations.AddField(
            model_name='project_detail',
            name='image4',
            field=models.ImageField(blank=True, upload_to=main.models.image_upload_detail4),
        ),
    ]