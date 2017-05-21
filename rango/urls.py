from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from rango import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login/$', auth_views.login, {'template_name':'rango/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),

    url(r'^about/', views.about),
    url(r'^noticeboard/$', views.show_notices, name='show_notices'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',views.show_category, name='show_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
    ]