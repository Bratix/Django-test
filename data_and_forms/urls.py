from django.urls import path

from . import views

app_name = "crud"

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('add/', views.AddUser.as_view(), name='add'),
    path('delete/<pk>', views.DeleteUser.as_view(), name = "delete"),
    path('edit/<pk>', views.EditUser.as_view(), name = "edit"),
]