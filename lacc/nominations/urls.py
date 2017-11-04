from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^students/$', views.student_list.as_view(), name='student_list'),
    url(r'^student/create/$', views.student_create.as_view(), name='student_create'),
    url(r'^student/(?P<pk>\d+)/$', views.student_details.as_view(), name='student_details'),
    url(r'^student/(?P<pk>\d+)/update/$', views.student_update.as_view(), name='student_update'),
    url(r'^student/(?P<pk>\d+)/delete/$', views.student_delete.as_view(), name='student_delete')
]
