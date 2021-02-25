# Generated by Django 3.1.6 on 2021-02-25 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0004_auto_20210224_1053'),
        ('profiles', '0007_auto_20210225_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='subscription',
            field=models.ForeignKey(default='bronze', on_delete=django.db.models.deletion.CASCADE, to='subscriptions.subscription'),
        ),
    ]