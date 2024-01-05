from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('register', views.register, name='register'),
    path('login', views.Login, name='login'),
    path('winter', views.winter, name='winter'),
    path('shipping', views.shipping, name='shipping'),
    path('confirmorder', views.confirmorder, name='confirmorder'),
    path('contactus', views.contactus, name='contactus'),
    path('logout', views.logout, name='logout'),
    path('newin', views.newin, name='newin'),
    path('productpage', views.productpage, name='productpage'),
    path('productpage2', views.productpage2, name='productpage2'),
    path('productpage3', views.productpage3, name='productpage3'),
    path('productpage4', views.productpage4, name='productpage4'),


]