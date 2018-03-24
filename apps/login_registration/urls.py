from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^',views.index, name = "index"),
    url(r'^success/$',views.success, name = "success"),
    url(r'^login_process/$', views.login_process, name = "login_process"),
    url(r'^register_process/$', views.register_process, name = "register_process"),
]