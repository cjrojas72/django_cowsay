from django.urls import path
from cowsay import views

urlpatterns = [
    path('', views.index, name='home'),
    path('history/', views.history)
]