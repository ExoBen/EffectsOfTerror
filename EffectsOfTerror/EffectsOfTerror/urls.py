from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'EffectsOfTerror.views.home', name='home'),
    url(r'^search/', 'EffectsOfTerror.views.search', name='search'),
    url(r'^graph/', 'EffectsOfTerror.views.graph', name='graph'),
)
