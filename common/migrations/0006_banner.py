# Generated by Django 5.1.7 on 2025-03-17 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_alter_footer_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='banner', verbose_name='баннер')),
                ('link', models.TextField(blank=True, null=True, verbose_name='Ссылка')),
                ('order', models.PositiveIntegerField(default=1, verbose_name='Порядок')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
    ]
