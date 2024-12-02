from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="home"),
    path(r'times/plus/<str:hours>',views.time_calc, name="time-calc"),
]
