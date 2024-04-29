from django.urls import path
from . import views

app_name = 'CICD'
urlpatterns = [
    path('test/', views.index, name='tes'),
]