from django.contrib import admin
from .models import Product, Banner, AnimeCon

admin.site.site_header = "Candy Fluffs Admin"
admin.site.site_title = "Admin"
admin.site.index_title = "Welcome Admin!"
# Register your models here.
admin.site.register(Product)
admin.site.register(Banner)
admin.site.register(AnimeCon)
