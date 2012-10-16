from django.conf.urls import patterns, url

urlpatterns = patterns('s3upload.views',
    url(r'^$', 'index', name='index'),
    url(r'^params$', 'get_upload_params', name='params'),
    url(r'^static/(?P<filename>[^/]+)$', 'static', name='static'),
)
