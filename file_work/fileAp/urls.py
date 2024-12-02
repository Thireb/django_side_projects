from django.urls import path
from . import views
from .views import QuoteDetailView
urlpatterns = [
    path('',views.formView,name='Form'),
    path('detail/<int:pk>',QuoteDetailView.as_view(),name='quote-detail'),
]
