from django.urls import path
from jobapp import views

urlpatterns = [

    path('', views.home, name='home')

]
