"""djangoUserRegisterLogin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^index/', views.index),
    url(r'^accounts/regist', views.register, name='register'),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout'),
    url(r'^accounts/forget_pass', views.forget_pass, name='forget_pass'),
    url(r'^accounts/reset_pass',views.reset_pass,name='reset_pass'),
    url(r'^accounts/change_pass/(?P<token>\w+.[-_\w]*\w+.[-_\w]*\w+)/$',views.change_pass,name='change_pass'),
    url(r'^accounts/do_chanage_pass',views.do_change_pass,name='do_change_pass'),
    url(r'^accounts/active/(?P<token>\w+.[-_\w]*\w+.[-_\w]*\w+)/$',views.active_user,name='active_user'),
]
