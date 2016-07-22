"""great_warrior_bot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from line_bot import views

urlpatterns = [
	url(r'^$', views.home_page, name='home'),
	url(r'^request/new$', views.form_page, name='request-form'),
	url(r'^request/confirm$', views.confirm_page, name='request-confirm'),
	url(r'^users/(?P<user_id>\d+)/orders$', views.orders_page, name='orders'),
    # url(r'^admin/', include(admin.site.urls)),
]
