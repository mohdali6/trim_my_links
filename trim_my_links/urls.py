from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^trim_link/$', views.trim_link, name='trim_link'),
]
