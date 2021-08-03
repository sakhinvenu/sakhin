from . import views
from django.urls import path

urlpatterns = [

    path('', views.demo123, name='demo123'),
    # path('', views.about, name='about'),
]
