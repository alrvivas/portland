from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),    
    url(r'^$', 'menus.views.index', name='index'),
    url(r'^pedidos/', include('pedidos.urls')), 
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^$', 'menus.views.login'),
    url(r'^logout/$', 'menus.views.logout'),
)