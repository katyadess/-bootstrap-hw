from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('demo/', views.demo, name='demo'),
    path('archives/', views.archives, name='archives'),
    path('blog/', views.blog, name='blog'),
    path('page/', views.page, name='page'),
    path('single/', views.single, name='single'),
    path('about', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
