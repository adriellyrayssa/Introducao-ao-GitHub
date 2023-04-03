from django.urls import path
from . import views

urlpatterns = [
    path('', views.Atividade1, name="Atividade1")

]