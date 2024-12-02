from .views import HomeView, DonorCreateView, DonorListView, DonorDetailView
from django.urls import path

urlpatterns = [
    path("<int:pk>/donor-detail/", DonorDetailView.as_view(), name="detail-donor"),
    path("list-donor/", DonorListView.as_view(), name="list-donor"),
    path('add-donor/',DonorCreateView.as_view(), name='add-donor'),
    path('', HomeView.as_view(), name='home'),
    
]

