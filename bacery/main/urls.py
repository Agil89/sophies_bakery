
from django.urls import path
from main.views import MainPageView,SubscriberCreateView,AboutUsView,ContactSubjectView,ContactPageView


app_name = 'main'


urlpatterns = [
    path('',MainPageView.as_view(),name='home'),
    path('subscribe/',SubscriberCreateView.as_view(),name='subscribe'),
    path('about/',AboutUsView.as_view(),name='about'),
    path('contact/',ContactPageView.as_view(),name='contact'),
    path('contact-form/',ContactSubjectView.as_view(),name='contact-form'),
]