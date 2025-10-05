from django.urls import path
from mapapp import views
urlpatterns = [
    path('', views.calculate_power, name='calculate_power'),
]