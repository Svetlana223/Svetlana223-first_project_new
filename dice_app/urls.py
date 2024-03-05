from django.urls import path
from . import views

urlpatterns = [
    path('gen_coin/<int:num>/', views.gen_coin, name="gen_coin"),
    path('gen_dice/<int:num>/', views.gen_dice, name="gen_dice"),
    path('gen_rand_hundred/<int:num>/', views.gen_rand_hundred, name="gen_rand_hundred"),
    path('game/', views.game, name='game')
]