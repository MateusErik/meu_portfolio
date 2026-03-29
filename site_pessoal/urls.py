from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('projetos/', views.projetos, name="projetos"),
    path('contatos/', views.contatos, name="contatos"),
    path('sobre/', views.sobre, name="sobre"),
]