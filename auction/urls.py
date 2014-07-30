from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'auction.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'', include('social_auth.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('account.urls', namespace='account')),

    url(r'^', include('core.urls', namespace='core')),
)

from auction import settings
urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
