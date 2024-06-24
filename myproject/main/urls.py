from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('demo/', views.demo, name='demo'),
    path('archives/', views.archives, name='archives'),
    path('blog/july', views.blog_july, name='blog'),
    path('blog/august', views.blog_august, name='blog_august'),
    path('page/', views.page, name='page'),
    path('single/', views.single, name='single'),
    path('about', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('faq', views.faq, name='faq')
]
