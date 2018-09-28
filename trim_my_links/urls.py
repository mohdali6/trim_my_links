from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^trim-link/$', views.trim_link, name='trim-link'),
	url(r'^trim-link/(?P<link_id>[0-9]+)/$', views.trim_link, name='trim-link'),
	url(r'^trim-link/result/$', views.redirect_to_result, name='redirect_to_result')
]
