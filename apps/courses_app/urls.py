from django.conf.urls import url,include
from . import views
urlpatterns = [
    url(r'^$',views.index,name = "index"),
    url(r'^courses/add$',views.add, name = "add"),
    url(r'^courses/destroy/(?P<courseid>\d+)$',views.prompt,name = "prompt"),
    url(r'^courses/destroy$',views.destroy,name = "destroy"),

]