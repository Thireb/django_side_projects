from django.urls import path
from . import views

app_name='polls'
urlpatterns = [
    #Home at index.html
    path('',views.Index.as_view(), name='index'),
    
    #Detail at detail.html
    path('<int:pk>/detail', views.Detail.as_view(), name='detail'),
    
    #Result at result.html 
    path('<int:pk>/result', views.Result.as_view(), name='result'),
    
    #Vote at 
    path('<int:question_id>/vote',views.vote, name='vote'),
    
]
