from rest_framework import serializers
from products.models import Cake,CupCake,Desert,DesertFeatures,CupCakeFeatures,CakeFeatures,EastSweets,\
    EastSweetFeatures,CakeTypes

class CakeFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = CakeFeatures
        fields = ('name',)

class CakeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CakeTypes
        fields = ('name',)

class CupCakeFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = CupCakeFeatures
        fields = ('name',)

class DesertFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = DesertFeatures
        fields = ('name',)

class SweetFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = EastSweetFeatures
        fields = ('name',)

class CakeSerializer(serializers.ModelSerializer):
    cake_features = CakeFeatureSerializer(many=True)
    cake_types = CakeTypeSerializer(many=True)
    class Meta:
        model = Cake
        fields = ('id',
                  'name',
                  'unit',
                  'name_of_unit',
                  'cake_features',
                  'cake_types',
                  'short_description',
                  'long_description',
                  'main_image',
                  'price',
                  'slug',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["my_url"] = instance.get_absolute_url()
        return data


class DesertSerializer(serializers.ModelSerializer):
    desert_features = DesertFeatureSerializer(many=True)

    class Meta:
        model = Desert
        fields = ('id',
                  'name',
                  'unit',
                  'name_of_unit',
                  'desert_features',
                  'short_description',
                  'long_description',
                  'main_image',
                  'price',
                  'slug',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["my_url"] = instance.get_absolute_url()
        return data

class SweetSerializer(serializers.ModelSerializer):
    eastSweetfeatures = SweetFeatureSerializer(many=True)

    class Meta:
        model = EastSweets
        fields = ('id',
                  'name',
                  'unit',
                  'name_of_unit',
                  'eastSweetfeatures',
                  'short_description',
                  'long_description',
                  'main_image',
                  'price',
                  'slug',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["my_url"] = instance.get_absolute_url()
        return data


class CupcakeSerializer(serializers.ModelSerializer):
    cupCakeFeature = CupCakeFeatureSerializer(many=True)

    class Meta:
        model = CupCake
        fields = ('id',
                  'name',
                  'unit',
                  'name_of_unit',
                  'cupCakeFeature',
                  'short_description',
                  'long_description',
                  'main_image',
                  'price',
                  'slug',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["my_url"] = instance.get_absolute_url()
        return data

