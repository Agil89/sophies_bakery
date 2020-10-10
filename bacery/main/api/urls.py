from django.urls import path
from main.api.views import SubscriberCreateAPIView,MainSearchAPIView

app_name = 'api_main'

urlpatterns = [
    path('subscribe/',SubscriberCreateAPIView.as_view(),name='subscribe'),
    path('allproducts/',MainSearchAPIView.as_view(),name='allproducts')
]