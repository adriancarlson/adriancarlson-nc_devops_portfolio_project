from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('intention/<str:pk>', views.intention, name="intention"),

    path('create-intention/', views.createIntention, name="create-intention"),
    path('update-intention/<str:pk>/', views.updateIntention, name="update-intention"),
    path('delete-intention/<str:pk>/', views.deleteIntention, name="delete-intention"),
    
    path('api/intentions/', views.intention_list),
    path('api/intentions/<int:pk>/', views.intention_detail),

]