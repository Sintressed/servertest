from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^users/(?P<user_id>\d+)$',views.user, name = "user"),
    #POST routes
    url(r'^process_login/$', views.process_login, name = "process_login"),
    url(r'^process_register/$', views.process_register, name = "process_register"),
]