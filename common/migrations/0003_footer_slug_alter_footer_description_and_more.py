# Generated by Django 5.1.7 on 2025-03-13 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_alter_footer_options_footer_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='footer',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='footer',
            name='description',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='footer',
            name='icon',
            field=models.ImageField(null=True, upload_to='footer/icons', verbose_name='Иконка'),
        ),
        migrations.AlterField(
            model_name='footer',
            name='link',
            field=models.TextField(null=True, verbose_name='Ссылка'),
        ),
    ]
