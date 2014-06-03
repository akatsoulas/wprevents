from django.conf.urls.defaults import url, patterns

from . import views

urlpatterns = patterns('',
  url(r'^calendar$', views.calendar, name='event_calendar'),
  url(r'^calendar_month$', views.calendar_month, name='event_calendar_month'),
  url(r'^search$', views.search, name='event_search'),
  url(r'^$', views.all, name='event_all'),
  url(r'^e/(?P<id>\w+)/(?P<slug>[a-z0-9-]+)$', views.one, name='event_one'),
)
