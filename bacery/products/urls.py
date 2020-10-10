from django.urls import path
from products.views import CakessListView,CupCakessListView,DesertssListView,SweetssListView,CakeDetailView,\
DesertDetailView,CupCakeDetailView,SweetDetailView
app_name = 'products_app'


urlpatterns = [
    path('cakes/',CakessListView.as_view(),name='cakes'),
    path('cupcakes/',CupCakessListView.as_view(),name='cupcakes'),
    path('deserts/',DesertssListView.as_view(),name='deserts'),
    path('sweets/',SweetssListView.as_view(),name='sweets'),
    path('cake-detail/<slug:slug>/',CakeDetailView.as_view(),name='cake-detail'),
    path('desert-detail/<slug:slug>/',DesertDetailView.as_view(),name='desert-detail'),
    path('cupcake-detail/<slug:slug>/',CupCakeDetailView.as_view(),name='cupcake-detail'),
    path('sweet-detail/<slug:slug>/',SweetDetailView.as_view(),name='sweet-detail'),
]