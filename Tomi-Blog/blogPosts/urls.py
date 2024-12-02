from django.urls import path
from . import views
urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login,name='login'),
    path('', views.login, name='login'),

    path('post/<str:pk>',views.post,name='post'),
    path('logout',views.logout,name='logout'),
    path('index',views.index,name='index'),
]
