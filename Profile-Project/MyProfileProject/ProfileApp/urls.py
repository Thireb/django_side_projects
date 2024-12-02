from django.urls import path
from . import views
app_name = 'ProfileApp'
urlpatterns = [
    path('', view = views.ProfileView.as_view(),name = 'ProFileApp'),
    ]
