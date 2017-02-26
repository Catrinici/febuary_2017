from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create$', views.create, name='create_course'),
    url(r'^descripton/delete/(?P<descripton_id>\d+)$', views.descripton_delete, name='delete_description'),
    url(r'^users_to_courses/$', views.add_users_to_courses, name = 'courses_has_users'),
]
