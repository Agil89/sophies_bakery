from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from products.api.serializers import CakeFeatureSerializer,CakeSerializer,SweetFeatureSerializer,SweetSerializer,\
    DesertFeatureSerializer,DesertSerializer,CupCakeFeatureSerializer,CupcakeSerializer
from products.models import Cake,CupCake,Desert,DesertFeatures,CupCakeFeatures,CakeFeatures,EastSweets,\
    EastSweetFeatures
import math
from rest_framework.response import Response
import requests
import json




class CakeListView(APIView):
    def get(self,request):
        data = request.GET
        cakeFeatures=data.getlist('cake_features[]')
        cakeTypes = data.getlist('cake_types[]')
        minPrice = data.get('minPrice')
        maxPrice = data.get('maxPrice')
        filtered_cakes = Cake.objects.all()
        if minPrice:
            filtered_cakes=filtered_cakes.filter(price__gte=minPrice).distinct()
        if maxPrice:
            filtered_cakes=filtered_cakes.filter(price__lte=maxPrice).distinct()
        if cakeFeatures:
            for cakeFeature in cakeFeatures:
                filtered_cakes = filtered_cakes.filter(cake_features__name=cakeFeature)
        if cakeTypes:
            for cakeType in cakeTypes:
                filtered_cakes = filtered_cakes.filter(cake_types__name=cakeType)

        print(filtered_cakes)
        cakes_count = filtered_cakes.count()
        cake_count_for_each_page = 6
        page_count = math.ceil(cakes_count/cake_count_for_each_page)
        page_range = range(1,page_count+1)

        page = data.get('page',1)
        if isinstance(page, str) and page.isdigit():
            page = int(page)
        cakes_for_each_page = filtered_cakes[(page-1)*6:page*6]
        serializered_cakes = CakeSerializer(cakes_for_each_page,many=True)
        return Response({
            'filtered_cakes': serializered_cakes.data,
            'page_range': page_count,
        })


class DesertListView(APIView):
    def get(self,request):
        data = request.GET
        desertFeatures=data.getlist('desert_features[]')
        minPrice = data.get('minPrice')
        maxPrice = data.get('maxPrice')
        filtered_deserts = Desert.objects.all()
        if minPrice:
            filtered_deserts=filtered_deserts.filter(price__gte=minPrice).distinct()
        if maxPrice:
            filtered_deserts=filtered_deserts.filter(price__lte=maxPrice).distinct()
        if desertFeatures:
            for desertFeature in desertFeatures:
                filtered_deserts = filtered_deserts.filter(desert_features__name=desertFeature)

        deserts_count = filtered_deserts.count()
        desert_count_for_each_page = 6
        page_count = math.ceil(deserts_count/desert_count_for_each_page)
        page_range = range(1,page_count+1)

        page = data.get('page',1)
        if isinstance(page, str) and page.isdigit():
            page = int(page)
        deserts_for_each_page = filtered_deserts[(page-1)*6:page*6]
        serializered_deserts = DesertSerializer(deserts_for_each_page,many=True)
        return Response({
            'filtered_deserts': serializered_deserts.data,
            'page_range': page_count,
        })


class CupCakeListView(APIView):
    def get(self,request):
        data = request.GET
        cupcakeFeatures=data.getlist('cupcake_features[]')
        minPrice = data.get('minPrice')
        maxPrice = data.get('maxPrice')
        filtered_cupcakes = CupCake.objects.all()
        if minPrice:
            filtered_cupcakes=filtered_cupcakes.filter(price__gte=minPrice).distinct()
        if maxPrice:
            filtered_cupcakes=filtered_cupcakes.filter(price__lte=maxPrice).distinct()
        if cupcakeFeatures:
            for cupcakeFeature in cupcakeFeatures:
                filtered_cupcakes = filtered_cupcakes.filter(cupCakeFeature__name=cupcakeFeature)

        cupcake_count = filtered_cupcakes.count()
        cupcake_count_for_each_page = 6
        page_count = math.ceil(cupcake_count/cupcake_count_for_each_page)
        page_range = range(1,page_count+1)

        page = data.get('page',1)
        print('BBBBBBBBBBBBBBBBBBBBBBBBBBBBB',page)
        if isinstance(page, str) and page.isdigit():
            page = int(page)
        cupcakes_for_each_page = filtered_cupcakes[(page-1)*6:page*6]
        serializered_cupcakes = CupcakeSerializer(cupcakes_for_each_page,many=True)
        return Response({
            'filtered_cupcakes': serializered_cupcakes.data,
            'page_range': page_count,
        })

class SweetsListView(APIView):
    def get(self,request):
        data = request.GET
        sweetFeatures=data.getlist('sweet_features[]')
        minPrice = data.get('minPrice')
        maxPrice = data.get('maxPrice')
        filtered_sweets = EastSweets.objects.all()
        if minPrice:
            filtered_sweets=filtered_sweets.filter(price__gte=minPrice).distinct()
        if maxPrice:
            filtered_sweets=filtered_sweets.filter(price__lte=maxPrice).distinct()
        if sweetFeatures:
            for sweetFeature in sweetFeatures:
                filtered_sweets = filtered_sweets.filter(eastSweetfeatures__name=sweetFeature)

        sweets_count = filtered_sweets.count()
        sweet_count_for_each_page = 6
        page_count = math.ceil(sweets_count/sweet_count_for_each_page)
        page_range = range(1,page_count+1)

        page = data.get('page',1)
        if isinstance(page, str) and page.isdigit():
            page = int(page)
        sweets_for_each_page = filtered_sweets[(page-1)*6:page*6]
        serializered_sweets = SweetSerializer(sweets_for_each_page,many=True)
        return Response({
            'filtered_sweets': serializered_sweets.data,
            'page_range': page_count,
        })