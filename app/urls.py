from django.urls import path
from .views import *

urlpatterns =[

    path('home/',home,name='home'),
    path('about/',about,name='about'),
    path('gellery/',gellery,name='gellery'),
    path('mywork/',mywork,name='mywork'),
    path('price/',price,name='price'),
    
]