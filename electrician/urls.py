from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('electrician/',views.electrician, name='electrician'),
    path('about/',views.about, name='about'),
    path('register/',views.registerpage,name='register'),
    path('login/',views.userlogin,name='login'),
    path('home/',views.home,name='home'),
    path('logout/',views.logoutuser,name='logout'),
    path('contact/', views.contact, name='contact'),
    path('create/', views.order_create, name='order_create'),
]