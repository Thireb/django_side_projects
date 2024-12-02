from unicodedata import name
from django.urls import path
from .views import HomeView,NotifListView, NotifUpdateView,NotifCreateView, NotifDeleteView
urlpatterns = [
    path('<int:pk>/delete/',NotifDeleteView.as_view(),name='delete_entry'),

    #path('', HomeView.as_view(),name='Home'),
    path('', NotifListView.as_view(),name='Users_list'),
    path('<int:pk>/update/', NotifUpdateView.as_view(),name='Users_list_update'),
    path('addnew/',NotifCreateView.as_view(),name='new_Entry'),    
]
