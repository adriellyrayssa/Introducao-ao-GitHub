from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('Atividade1', include('Atividade1.urls')),
    path('Atividade2', include('Atividade2.urls')),
]
