from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.all_shows),
    url(r'^shows/new$', views.new_show),
    url(r'^shows/create$', views.shows_create),
    url(r'^shows$', views.all_shows),
    url(r'^shows/(?P<show_id>\d+)/edit$', views.edit_show),
    url(r'^shows/(?P<show_id>\d+)/update$', views.update_show),
    url(r'^shows/(?P<show_id>\d+)/destroy$', views.destroy_show),
    url(r'^shows/(?P<show_id>\d+)$', views.shows_id),
]