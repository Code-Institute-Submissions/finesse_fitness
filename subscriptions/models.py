from django.db import models
from django.contrib.auth.models import User

# Add for clean method to add custom validation
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Subscription(models.Model):
    """
    Creates a subscriptions type model with the different type of subscriptions
    """

    gold = 'gold'
    silver = 'silver'
    bronze = 'bronze'
    access = [
        (gold, 'gold'),
        (silver, 'silver'),
        (bronze, 'bronze'),
    ]

    yes = 'yes'
    no = 'no'
        
    foc_delivery = [
        (yes, 'yes'),
        (no, 'no'),
    ]

    blog_access = [
        (no, 'no'),
        (yes, 'yes'),
    ]

    subscription_level = models.CharField(max_length=10)
    image = models.ImageField('Subscription Picture', null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    priority = models.CharField(max_length=10, choices=access)
    first_order_discount=models.IntegerField('First Order Discount', default=0)
    shop_discount = models.IntegerField(default=0)
    free_delivery = models.CharField(max_length=3, choices=foc_delivery, default=no)
    blog = models.CharField(max_length=3, choices=blog_access)

    def __str__(self):
        return self.subscription_level


    def clean(self):
        """
        Show error if the user enters discounts or prices below 0
        """
        if self.price and self.price < 0:
            raise ValidationError(_("Price can't be negative"))
        elif self.first_order_discount and self.first_order_discount < 0:
            raise ValidationError(_("First Order Discount"
                                    " Value can't be negative"))
        elif self.shop_discount and self.shop_discount < 0:
            raise ValidationError(_("Overall Discount"
                                    " Value can't be negative"))

    

class StripeCustomer(models.Model):
    """
    Create a model to store customer information needed
    for Stripe Subscription payments
    """
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    stripeCustomerId = models.CharField(max_length=255)
    stripeSubscriptionId = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username
