from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^add$', views.add, name = "add"),
    url(r'^(?P<book_id>\d+)$', views.view, name = "view"),
    #post routes
    url(r'^add_process$', views.add_process, name = "add_process"),
    url(r'^delete$', views.delete_process, name = "delete_process"),

]