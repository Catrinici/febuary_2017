from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'no_ninjas'),
    url(r'^ninjas/$', views.show, name='all_ninjas'),
    url(r'^ninjas/(?P<ninja>\w+)$', views.showOne, name='show_ninja')
]
