from django.db import models
from products.tools.slug_generator import slugify
from datetime import datetime
from django.urls import reverse_lazy

class CakeFeatures(models.Model):
    #information
    name = models.CharField('Name',max_length=40)

    class Meta:
        verbose_name = 'CakeFeature'
        verbose_name_plural = 'CakeFeatures'

    def __str__(self):
        return self.name

class CakeTypes(models.Model):
    #information
    name = models.CharField('Name',max_length=40)

    class Meta:
        verbose_name = 'CakeType'
        verbose_name_plural = 'CakeTypes'

    def __str__(self):
        return self.name

# Create your models here.
class Cake(models.Model):
    #information
    name= models.CharField('Name',max_length=50)
    short_description = models.CharField('Short Description',max_length=500)
    unit=models.PositiveSmallIntegerField('Unit')
    name_of_unit=models.CharField('Unit name',max_length=50)
    long_description = models.TextField('Long Description')
    main_image = models.ImageField('Main image',upload_to='images/cakeImages')
    price = models.PositiveSmallIntegerField('Price')

    #relations
    cake_features=models.ManyToManyField(CakeFeatures,verbose_name='Cake Feature',related_name='cakes')
    cake_types = models.ManyToManyField(CakeTypes, verbose_name='Cake Type', related_name='cakes')
    #moderations
    slug = models.SlugField('slug', max_length=255, editable=False, unique=True)

    class Meta:
        verbose_name = 'Cake'
        verbose_name_plural = 'Cakes'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = f'{slugify(self.name)}-{datetime.now().strftime("%Y%m%d-%H%M%S")}'
        super().save()

    # YOU HAVE TO CHANGE THIS URL
    def get_absolute_url(self):
        return reverse_lazy('products_app:cake-detail',kwargs={'slug':self.slug})

class DesertFeatures(models.Model):
    #information
    name = models.CharField('Name',max_length=40)

    class Meta:
        verbose_name = 'DesertFeature'
        verbose_name_plural = 'DesertFeatures'

    def __str__(self):
        return self.name



# Create your models here.
class Desert(models.Model):
    #information
    name= models.CharField('Name',max_length=50)
    short_description = models.CharField('Short Description',max_length=500)
    unit = models.PositiveSmallIntegerField('Unit')
    name_of_unit = models.CharField('Unit name', max_length=50)
    long_description = models.TextField('Long Description')
    main_image = models.ImageField('Main image',upload_to='images/desertImages')
    price = models.PositiveSmallIntegerField('Price')

    #relations
    desert_features=models.ManyToManyField(DesertFeatures,verbose_name='Desert Feature',related_name='deserts')

    #moderations
    slug = models.SlugField('slug', max_length=255, editable=False, unique=True)

    class Meta:
        verbose_name = 'Desert'
        verbose_name_plural = 'Deserts'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = f'{slugify(self.name)}-{datetime.now().strftime("%Y%m%d-%H%M%S")}'
        super().save()



    #YOU HAVE TO CHANGE THIS URL
    def get_absolute_url(self):
        return reverse_lazy('products_app:desert-detail', kwargs={'slug': self.slug})


class EastSweetFeatures(models.Model):
    #information
    name = models.CharField('Name',max_length=40)

    class Meta:
        verbose_name = 'EastSweetFeature'
        verbose_name_plural = 'EastSweetFeatures'

    def __str__(self):
        return self.name



# Create your models here.
class EastSweets(models.Model):
    #information
    name= models.CharField('Name',max_length=50)
    short_description = models.CharField('Short Description',max_length=500)
    long_description = models.TextField('Long Description')
    unit = models.PositiveSmallIntegerField('Unit')
    name_of_unit = models.CharField('Unit name', max_length=50)
    main_image = models.ImageField('Main image',upload_to='images/eastSweetImages')
    price = models.PositiveSmallIntegerField('Price')

    #relations
    eastSweetfeatures=models.ManyToManyField(EastSweetFeatures,verbose_name='EastSweet Feature',related_name='eastSweets')

    #moderations
    slug = models.SlugField('slug', max_length=255, editable=False, unique=True)

    class Meta:
        verbose_name = 'EastSweet'
        verbose_name_plural = 'EastSweets'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = f'{slugify(self.name)}-{datetime.now().strftime("%Y%m%d-%H%M%S")}'
        super().save()


    #YOU HAVE TO CHANGE THIS URL
    def get_absolute_url(self):
        return reverse_lazy('products_app:sweet-detail', kwargs={'slug': self.slug})


class CupCakeFeatures(models.Model):
    #information
    name = models.CharField('Name',max_length=40)

    class Meta:
        verbose_name = 'CupCakeFeature'
        verbose_name_plural = 'CupCakeFeatures'

    def __str__(self):
        return self.name



# Create your models here.
class CupCake(models.Model):
    #information
    name= models.CharField('Name',max_length=50)
    short_description = models.CharField('Short Description',max_length=500)
    long_description = models.TextField('Long Description')
    unit = models.PositiveSmallIntegerField('Unit')
    name_of_unit = models.CharField('Unit name', max_length=50)
    main_image = models.ImageField('Main image',upload_to='images/CupCakeImages')
    price = models.PositiveSmallIntegerField('Price')

    #relations
    cupCakeFeature=models.ManyToManyField(CupCakeFeatures,verbose_name='CupCake Feature',related_name='cupcakes')

    #moderations
    slug = models.SlugField('slug', max_length=255, editable=False, unique=True)

    class Meta:
        verbose_name = 'CupCake'
        verbose_name_plural = 'CupCakes'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = f'{slugify(self.name)}-{datetime.now().strftime("%Y%m%d-%H%M%S")}'
        super().save()


    #YOU HAVE TO CHANGE THIS URL
    def get_absolute_url(self):
        return reverse_lazy('products_app:cupcake-detail', kwargs={'slug': self.slug})


