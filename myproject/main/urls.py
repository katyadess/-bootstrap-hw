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
    path('single/white_space_everywhere', views.single_one, name='single_one'),
    path('single/Simple_And_Minimalist_Designs', views.single_two, name='single_two'),
    path('single/Hey, We Love Open Sans!', views.single_three, name='single_three'),
    path('single/Hey, We Love Roboto!', views.single_four, name='single_four'),
    path('single/Simplicity and Elegance in Design', views.single_five, name='single_five'),
    path('about', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('faq', views.faq, name='faq'),
    path('wordpress/', views.wordpress, name='wp'),
    path('ghost/', views.ghost, name='ghost'),
    path('joomla/', views.joomla, name='joomla'),
    path('magento/', views.magento, name='magento')
]
