from django.db import models
from django.contrib.auth.models import User

# ADD FANDOMS HERE * KEYS MUST BE UNIQUE *
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

# ADD PRODUCT TYPES HERE * KEYS MUST BE UNIQUE *
PRODUCT_TYPES = (
    ('M', 'Misc'),
    ('B', 'Buttons')
)

# Create your models here.


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
    # is integer right here? yes, the weight will be in ounces as whole numbers!
    weight = models.IntegerField()
    size = models.CharField(max_length=200)
    created_date = models.DateTimeField('Created on')

# featured images for homepage


class Banner(models.Model):
    title = models.CharField(max_length=270)
    featured = models.ImageField()
    created_date = models.DateTimeField('Created on')

# Convention and live events


class AnimeCon(models.Model):
    eventName = models.CharField(max_length=270)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    eventTicets = models.URLField()
    description = models.TextField()
    created_date = models.DateTimeField('Created on')
