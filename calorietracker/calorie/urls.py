from django.urls import path
from . import views

# Hier maak path's aan. Dit gebruik ik voor om de gebruiker naar een andere pagina te sturen.
urlpatterns = [
    path('', views.index, name='index'),
    path('account/', views.account, name='account'),
    path('tracker/', views.tracker,name='tracker'),
]




