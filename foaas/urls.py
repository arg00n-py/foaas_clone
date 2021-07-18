from django.urls import path
from . import views

app_name = 'foaas'

urlpatterns = [
    path('', views.index, name="index"),
    path('fu/<str:name>/<str:sender>', views.fuck_you, name="fu"),
    path('awesome/<str:name>/<str:sender>', views.awesome, name="awesome"),
    path('sfu/<str:name>/<str:sender>', views.sfu, name="sfu"),
    path('dalton/<str:name>/<str:sender>', views.dalton, name="datlon"),
    path('ballmer/<str:name>/<str:pronoun>/<str:sender>', views.ballmer, name="ballmer"),
    path('dalton/<str:name>/<str:sender>', views.dalton, name="dalton"),
]
