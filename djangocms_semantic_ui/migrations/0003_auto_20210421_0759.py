# Generated by Django 3.2 on 2021-04-21 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_semantic_ui', '0002_card_cardcontainer'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='photo',
            field=models.ImageField(null=True, upload_to='user_photos', verbose_name='User photo'),
        ),
        migrations.AlterField(
            model_name='card',
            name='right_bottom_content',
            field=models.CharField(blank=True, help_text='Additional content displayed in right bottom corner of the card', max_length=32, null=True, verbose_name='Right bottom content'),
        ),
    ]
