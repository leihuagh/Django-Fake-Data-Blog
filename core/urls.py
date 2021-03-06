from django.urls import path
from home.views import index
from company.views import about, contact
from authentication.views import login_view, logout_view
from accounts.views import register

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('login', login_view, name='login'),
    path('register', register, name='register'),
    path('logout', logout_view, name='logout'),
]
