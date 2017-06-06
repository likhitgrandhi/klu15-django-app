from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from rango import views

urlpatterns = [
    url(r'^$', views.show_notices),
    url(r'^login/$', auth_views.login, {'template_name':'rango/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^register/$', views.register, name='register'),

    url(r'^about/', views.about),
    url(r'^noticeboard/$', views.show_notices, name='show_notices'),
    url(r'^category/(?P<course_name_slug>[\w\-]+)/$',views.show_course, name='show_course'),
    url(r'^category/(?P<course_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
    ]