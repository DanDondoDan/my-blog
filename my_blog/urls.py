"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from my_blog.views import article as views
from my_blog.views.article import SubscribeView, BlogView, PostCreateView, PostDetailView, HomeView, PostReadView, PostDeleteView
from django.conf.urls.static import static
from my_blog import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^subscribe/$', SubscribeView.as_view(), name='subscribe'),
    url(r'^blog/create/$', PostCreateView.as_view(), name='create'),
    url(r'^blog/read/$', PostReadView.as_view(), name='read'),
    url(r'^blog/(?P<pk>[0-9]+)/$', BlogView.as_view(), name='user'),
    url(r'^blog/(?P<pk>[0-9]+)/delete/$', PostDeleteView.as_view(), name='delete'),
    url(r'^blog/(?P<user_id>[0-9]+)/(?P<pk>[0-9]+)/$', PostDetailView.as_view(), name='detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
