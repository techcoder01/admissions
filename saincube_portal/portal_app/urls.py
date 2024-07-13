from django.urls import include, path
from . import views

# Create your views here.
urlpatterns = [
    path('', views.home, name='home'),
    path('apply/', views.apply, name='apply'),
]