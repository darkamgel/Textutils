from django.contrib import admin
from django.urls import path, include
from home import views
from home import sqli_lab

sqli_urlpatterns = [
    path(f'sqli/{i:03d}', view, name=f'sqli_{i:03d}')
    for i, view in enumerate(sqli_lab.SQLI_VULN_VIEWS, start=1)
]

urlpatterns = [
    path('', views.home, name="home"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('search', views.search, name="search"),
    path('lookupContact', views.lookupContact, name="lookupContact"),
    path('lookupUser', views.lookupUser, name="lookupUser"),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handleLogin, name="handleLogin"),
    path('logout', views.handleLogout, name="handleLogout"),
] + sqli_urlpatterns
