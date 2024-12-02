from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    # path('', views.index, name='index'),
    path('testpage', TemplateView.as_view(template_name = 'pages/page.html')),
    path('', views.index, {'pagename': ''}, name='home'),
    path('contact', views.contact, name='contact'),
    path('<str:pagename>', views.index, name='index'),
]
