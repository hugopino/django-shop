from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path('services/', views.services, name='services'),
    path('shop/', views.shop, name='shop'),
    path('blog/', views.blog, name='shop'),
    path('contact/', views.contact, name='contact'),
]