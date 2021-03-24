from django.urls import path
from . import views


# 네임 스페이스
app_name = 'members'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('mypage/<str:username>/', views.mypage, name='mypage'),
    path('mypageEdit/<str:username>/', views.mypageEdit, name='mypageEdit'),
    path('logout/', views.logout, name='logout')
]