from django.urls import path
from . import views

# Hier maak path's aan. Dit gebruik ik voor om de gebruiker naar een andere pagina te sturen.

urlpatterns = [
    # Dit is de homepage
    path('', views.index, name='index'),
    # Dit is de account pagina
    path('account/', views.account, name='account'),
    # Dit is de tracker pagina
    path('tracker/', views.tracker,name='tracker'),
]



