from django.conf.urls import url
from django.urls import path, re_path
from users.views import register
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from bazar.views import home

urlpatterns = [
	path('register/', register, name='register'),
	path('register/success', TemplateView.as_view(template_name='success.html'), name='registersuccess'),
	path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), {'next_page': 'index.html'}, name='logout'),
	path('accounts/profile/', TemplateView.as_view(template_name='index.html'), name='loginredirect')
]