from django.conf.urls.defaults import url, patterns

from . import views

urlpatterns = patterns('',
  url(r'^calendar$', views.calendar, name='event_calendar'),
  url(r'^$', views.all, name='event_all'),
  url(r'^e/(?P<slug>[a-z0-9-]+)$', views.one, name='event_one'),
)