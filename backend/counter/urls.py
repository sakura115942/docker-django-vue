from xml.etree.ElementInclude import include
from django.urls import path
from .views import CounterViewSet
from django.conf.urls import url


urlpatterns = [
    url("count", CounterViewSet)
]
