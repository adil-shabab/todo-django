from . import views
from django.urls import path

urlpatterns = [
    path('accounts/login', views.login, name='login'),
    path('accounts/signup', views.signup, name='signup'),
    path('accounts/logout', views.logoutUser, name='logout'),
    path('', views.home, name='home'),
    path('update_task/<str:pk>', views.updatetask, name='update'),
    path('delete/<str:pk>', views.deletetask, name='delete'),
    path('complete/<str:pk>', views.completetask, name='complete'),
]