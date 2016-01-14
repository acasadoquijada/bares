from django.conf.urls import patterns, url
from bares import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/', views.about, name='about'),
        url(r'^add_tapa/$', views.add_tapa, name='add_tapa'), # NEW MAPPING!
        url(r'^reclama_datos/', views.reclama_datos, name='reclama_datos'),
        url(r'^bar/(?P<bar_name_slug>[\w\-]+)/$', views.bares, name='bares'))  # New!
        
