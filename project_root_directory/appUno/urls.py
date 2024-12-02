from django.urls import path
from . import views


urlpatterns = [
    path("displayForm", views.displayForm, name="displayFormData"),
    path("contact", views.contactFormView, name="contact"),
    path('<str:pagename>',views.index,name='home')
    
]
