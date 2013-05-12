from django.conf.urls import patterns, url
from example_app.views import sample_view

urlpatterns = patterns('',
                       url(r'^$', sample_view.index, name='index'),
                       )
