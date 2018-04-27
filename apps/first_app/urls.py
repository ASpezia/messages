from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$',views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout), #render the logout page
    url(r'^logoutfunc$', views.logoutfunc), #process the logic .
    url(r'^messages$', views.messages),
    url(r'^profile/(?P<id>\d+)$', views.edit_msg),
    url(r'^delete_msg/(?P<id>\d+)$', views.delete_msg),
    url(r'^add$', views.add),
    url(r'^save_msg/(?P<id>\d+)$', views.save_msg)
]
