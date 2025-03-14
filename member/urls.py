from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('add/add_to_model/', views.add_to_model, name='add_to_model'),
    path('update/<int:id>/', views.update, name='update'),
    path('update/update_to_model/<int:id>/', views.update_to_model, name='update_to_model'),
    path('delete_to_model/<int:id>/', views.delete_to_model, name='delete_to_model'),
]