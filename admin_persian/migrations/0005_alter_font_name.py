# Generated by Django 4.0.6 on 2022-07-30 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_persian', '0004_alter_font_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='font',
            name='name',
            field=models.CharField(choices=[('sahel', 'ساحل'), ('yekan', 'یکان'), ('parastoo', 'پرستو'), ('samim', 'صمیم'), ('shabnam', 'شبنم'), ('tanha', 'تنها'), ('vazir', 'وزیر')], default='sahel', max_length=10, verbose_name='انتخاب فونت'),
        ),
    ]
