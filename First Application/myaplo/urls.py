from django.urls import path
from . import views
urlpatterns = [
    path('index',views.index,name='home'),
    path('counter',views.counter,name='counter'),
    path('block/',views.blockView,name='block-page'),
    path('space/',views.spaceView,name='space'),
    path('register',views.register,name='register'),
    path('login',views.loginView,name='login'),
    path('logout',views.logoutView,name='logout'),
]
