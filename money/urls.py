"""money URL Configuration

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
from moneymanage import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.log_in, name='login'),
    url(r'^register$', views.register, name='register'),
    url(r'^register2$', views.register2, name='register2'),
    url(r'^(?P<user_name>\w+)/logout$', views.logout_view, name='logout'),
    url(r'^(?P<user_name>\w+)/$', views.home, name='home'),
    url(r'^(?P<user_name>\w+)/saving/$', views.saving, name='saving'),
    url(r'^(?P<user_name>\w+)/gold/$', views.gold, name='gold'),
    url(r'^(?P<user_name>\w+)/stock/$', views.stock, name='stock'),
    url(r'^(?P<user_name>\w+)/bank/$', views.bank, name='bank'),
    url(r'^(?P<user_name>\w+)/saving/delete$', views.delete, name='delete'),
]
