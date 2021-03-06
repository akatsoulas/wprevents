from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http import HttpResponse

from funfactory.monkeypatches import patch
patch()

from base import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

handler404 = views.error404
handler500 = views.error500

urlpatterns = patterns('',
  (r'', include('django_browserid.urls')),
  (r'', include('wprevents.events.urls')),
  (r'', include('wprevents.base.urls')),

  # API
  url(r'^api/', include('wprevents.api.urls')),
  (r'^admin/', include('wprevents.admin.urls')),


  # Generate a robots.txt
  (r'^robots\.txt$', lambda r: HttpResponse(
    "User-agent: *\n%s: /" % 'Allow' if settings.ENGAGE_ROBOTS else 'Disallow' ,
    mimetype="text/plain")
  ),
  url(r'^404$', handler404, name='404'),
  url(r'^500$', handler500, name='500'),
  # Uncomment the admin/doc line below to enable admin documentation:
  # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

  # Uncomment the next line to enable the admin:
  # (r'^admin/', include(admin.site.urls)),
)

## In DEBUG mode, serve media files through Django.
if settings.DEBUG:
  urlpatterns += staticfiles_urlpatterns()

  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)