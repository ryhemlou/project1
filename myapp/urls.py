from django.urls import path, include
from . import views
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

urlpatterns=[
    path('', views.index, name='index'),
    path('counter', views.counter, name='counter'),
    path('register', views.register, name='register'),



    

    path('login', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('counter1',views.counter1, name='counter1'),
    path('', TemplateView.as_view(template_name="google.html")),
    #dynamic url now
    path('post/<str:pk>', views.post, name='post'),

    #path('', TemplateView.as_view(template_name="index.html")),

    #path('accounts/login/google/callback/', views.google_login_callback, name='google_login_callback'),
]

    #...
    
