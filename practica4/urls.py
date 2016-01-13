"""practica4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import patterns,include, url
from django.contrib import admin
from registration.backends.simple.views import RegistrationView
from django.conf import settings

# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/bares/'


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bares/', include('bares.urls')),
        #Add in this url pattern to override the default pattern in accounts.
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')))
    
    
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )

   
    
    
    
    
    
    
    
    
