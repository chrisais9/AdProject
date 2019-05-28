from django.conf.urls import url
from WordWarAPI import views

urlpatterns = [
    url(r'^login/$', views.signin, name='login'),
    url(r'^join/$', views.signup, name='join'),
    url(r'^$', views.index, name = 'index'),
]