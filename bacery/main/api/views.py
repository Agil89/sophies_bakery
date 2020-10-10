from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from main.api.serializers import SubscriberSerializer
from products.api.serializers import CakeSerializer,DesertSerializer,SweetSerializer,CupcakeSerializer
from rest_framework.authentication import BasicAuthentication
from main.api.utils import CsrfExemptSessionAuthentication
from products.models import Cake,Desert,CupCake,EastSweets
from itertools import chain
from rest_framework.response import Response

class SubscriberCreateAPIView(CreateAPIView):
    authentication_classes = (CsrfExemptSessionAuthentication,BasicAuthentication)
    serializer_class = SubscriberSerializer


class MainSearchAPIView(APIView):
    def get(self, request):
        input_value = self.request.GET.get('inputValue')
        print(input_value)

        cake_query = Cake.objects.filter(name__icontains=input_value)[:2]
        desert_query = Desert.objects.filter(name__icontains=input_value)[:2]
        cupcake_query = CupCake.objects.filter(name__icontains=input_value)[:2]
        sweet_query = EastSweets.objects.filter(name__icontains=input_value)[:2]

        cake_serializer = CakeSerializer(cake_query, many=True, context={'request': request})
        desert_serializer = DesertSerializer(desert_query, many=True,context={'request': request})
        cupcake_serializer = CupcakeSerializer(cupcake_query, many=True, context={'request': request})
        sweet_serializer = SweetSerializer(sweet_query, many=True, context={'request': request})


        data_obj = list(
            chain(cake_serializer.data, desert_serializer.data, cupcake_serializer.data, sweet_serializer.data, ))

        data = {
            "data_obj": data_obj,
        }
        print(data)
        return Response(data)