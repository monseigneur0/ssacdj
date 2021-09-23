# Generated by Django 3.2.6 on 2021-09-02 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', '남성(men)'), ('W', '여성(women')], max_length=1, verbose_name='성별'),
        ),
    ]