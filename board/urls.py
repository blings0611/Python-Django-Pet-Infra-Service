from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('list/', views.p_list, name='p_list'),
    path('list2/', views.phr_list, name='phr_list'),
    path('list3/', views.pps_list, name='pps_list'),

    path('create/', views.p_create, name='p_create'),
    path('create2/', views.phr_create, name='phr_create'),
    path('create3/', views.pps_create, name='pps_create'),

    path('detail/<int:post_id>', views.p_detail, name='p_detail'),
    path('detail2/<int:post_id>', views.phr_detail, name='phr_detail'),
    path('detail3/<int:post_id>', views.pps_detail, name='pps_detail'),

    path('update/<int:post_id>', views.p_update, name='p_update'),
    path('update2/<int:post_id>', views.phr_update, name='phr_update'),
    path('update3/<int:post_id>', views.pps_update, name='pps_update'),

    path('delete/<int:post_id>', views.p_delete, name="p-delete"),
    path('delete2/<int:post_id>', views.phr_delete, name="phr-delete"),
    path('delete3/<int:post_id>', views.pps_delete, name="pps-delete"),
]