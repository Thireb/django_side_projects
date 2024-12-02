from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    # ex: localhost:8000/polls/
    path('', views.IndexView.as_view(), name = 'index'),
    # ex: localhost:8000/polls/5
    # 'name' value as called by {% url %} in index.html template tag
    path('<int:pk>/', views.DetailView.as_view(), name= 'detail'),
    # ex: localhost:8000/polls/5/results
    path('<int:pk>/results/', views.ResultsView.as_view(), name = 'results'),
    # ex: localhost:8000/polls/5/votes
    path('<int:question_id>/vote/', views.vote, name = 'vote'),

]