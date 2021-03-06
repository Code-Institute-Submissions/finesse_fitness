# Generated by Django 3.1.6 on 2021-02-21 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscription_level', models.CharField(max_length=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Subscription Picture')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('priority', models.CharField(choices=[('gold', 'gold'), ('silver', 'silver'), ('bronze', 'bronze')], max_length=10)),
                ('first_order_discount', models.IntegerField(default=0, verbose_name='First Order Discount')),
                ('shop_discount', models.IntegerField(default=0)),
                ('free_delivery', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='no', max_length=3)),
                ('blog', models.CharField(choices=[('no', 'no'), ('yes', 'yes')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='StripeCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripeCustomerId', models.CharField(max_length=255)),
                ('stripeSubscriptionId', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
