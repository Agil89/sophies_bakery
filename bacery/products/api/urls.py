from django.urls import path
from products.api.views import CakeListView,DesertListView,CupCakeListView,SweetsListView

app_name = 'api_products'

urlpatterns = [
    path('cakes/',CakeListView.as_view(),name='cakes'),
    path('deserts/',DesertListView.as_view(),name='deserts'),
    path('cupcakes/',CupCakeListView.as_view(),name='cupcakes'),
    path('sweets/',SweetsListView.as_view(),name='sweets'),
]