"""beckett URL Configuration

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
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import ListView
from django.views.generic.base import RedirectView
from apps.letters import views
#admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='/letters', permanent=False)), # temp redirect to letters
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^people/', include('beckett.apps.people.urls', namespace="persons")),
    url(r'^letters/', include('beckett.apps.letters.urls', namespace="lettering")),
    url(r'^place/', include('beckett.apps.geo.urls', namespace="geo")),
    url(r'^events/', include('beckett.apps.events.urls', namespace="events")),
    url(r'^works/', include('beckett.apps.works.urls', namespace="works")),
    url(r'^api/search/', views.get_search_autocomplete),

#    url(r'^(?P<doc_id>[^/]+)$', views.letter_display, name="letter_display"),
)
