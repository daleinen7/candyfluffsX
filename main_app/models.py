from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

#### ADD FANDOMS HERE * KEYS MUST BE UNIQUE *
FANDOMS = (
    ('H', 'My Hero Academia'),
    ('M', 'Miraculous Lady'),
    ('S', 'Sailor Moon'),
    ('V', 'Vampire Hunter D'),
    ('J', 'JoJo\'s Bizarre Adventure'),
    ('H', 'Haikyuu'),
    ('K', 'Kingdom Hearts'),
    ('N', 'Necahual'),
    ('F', 'Final Fantasy'),
    ('C', 'Castlevania')
)

#### ADD PRODUCT TYPES HERE * KEYS MUST BE UNIQUE *
PRODUCT_TYPES = (
    ('M', 'Misc'),
    ('B', 'Buttons')
)

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    billing_address = models.CharField(max_length=200)
    default_shipping_address = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    phone = models.CharField(max_length=11)
    signup_date = models.DateTimeField('Signed Up On')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Product(models.Model):
    title = models.CharField(max_length=270)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.ImageField()
    fandom = models.CharField(max_length=1, choices=FANDOMS)
    product_type = models.CharField(max_length=1, choices=PRODUCT_TYPES)
    variation = models.CharField(max_length=200)
    stock = models.IntegerField()
    sku = models.IntegerField()
    weight = models.IntegerField() # is integer right here? yes, the weight will be in ounces as whole numbers!
    size = models.CharField(max_length=200)
    created_date = models.DateTimeField('Created on')

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    total = models.IntegerField()
    shipping_address = models.CharField(max_length=200)
    order_address = models.CharField(max_length=200)
    order_email = models.CharField(max_length=200)
    order_date = models.DateTimeField('Order Date')
    order_status = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
