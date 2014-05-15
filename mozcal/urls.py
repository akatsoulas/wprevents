from django.conf import settings
from django.conf.urls.defaults import patterns, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from funfactory.monkeypatches import patch
patch()

from events.api import EventResource

event_resource = EventResource()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
  (r'^api/', include(event_resource.urls)),
  (r'', include('mozcal.events.urls')),
  (r'^browserid/', include('django_browserid.urls')),

  # Generate a robots.txt
  (r'^robots\.txt$', lambda r: HttpResponse(
    "User-agent: *\n%s: /" % 'Allow' if settings.ENGAGE_ROBOTS else 'Disallow' ,
    mimetype="text/plain")
  )

  # Uncomment the admin/doc line below to enable admin documentation:
  # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

  # Uncomment the next line to enable the admin:
  # (r'^admin/', include(admin.site.urls)),
)

## In DEBUG mode, serve media files through Django.
if settings.DEBUG:
  urlpatterns += staticfiles_urlpatterns()
