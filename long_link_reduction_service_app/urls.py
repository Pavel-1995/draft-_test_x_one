

from django.urls import path
from .import views
from .views import logout_user

urlpatterns = [

    path('', views.index, name='home'),  #название маршрута
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),

]