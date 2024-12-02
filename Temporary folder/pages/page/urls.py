from django.urls import path
from . import views

urlpatterns = [
    #path('',views.index ,name='index'),
    path('', views.index, {'pagenumber': ''}, name= 'home'),
    path('<str:pagenumber>', views.index, name='newpage')
]
