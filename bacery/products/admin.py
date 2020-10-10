from django.contrib import admin
from products.models import CakeFeatures,CupCakeFeatures,CupCake,Cake,\
    DesertFeatures,Desert,EastSweetFeatures,EastSweets,CakeTypes
# Register your models here.
admin.site.register(CakeFeatures)
admin.site.register(CakeTypes)
admin.site.register(CupCakeFeatures)
admin.site.register(DesertFeatures)
admin.site.register(EastSweetFeatures)
admin.site.register(Cake)
admin.site.register(CupCake)
admin.site.register(Desert)
admin.site.register(EastSweets)



