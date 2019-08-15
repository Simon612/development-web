from django.urls import path

from . import views

urlpatterns = [
    path('aboutme/', views.aboutme, name='aboutme'),
    path('',views.homepage, name='homepage'),
    path('signed/', views.signed, name='signed'),
    path('list/', views.list, name='list'),
    path('homepage2/',views.homepage2, name='homepage2'),
]