from django.urls import path
from . import views

app_name = 'themes'

urlpatterns = [
    path('', views.themes, name='themes'),
    path('dataInsert/', views.data_insert, name='data_insert'),
    path('hotel/', views.hotel_list, name='hotel_list'),
    path('training/', views.training_list, name='training_list'),
    path('cafe/', views.cafe_list, name='cafe_list'),
    path('<int:local_id>/', views.t_object, name='t_object')
]
