from django.db import models
from django.contrib.auth.models import User

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
class Product(models.Model):
    title = models.CharField(max_length=270)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.FileField(upload_to='uploads/')
    fandom = models.CharField(max_length=1, choices=FANDOMS),
    product_type = models.CharField(max_length=1, choices=PRODUCT_TYPES)
    variation = models.CharField(max_length=200)
    stock = models.IntegerField()
    sku = models.IntegerField()
    weight = models.IntegerField() # is integer right here? yes, the weight will be in ounces as whole numbers!
    size = models.CharField(max_length=200)
    created_date = models.DateTimeField('Created on')


