from django.conf.urls import url,include
from apps.inicio.views import index, special, user_login, user_logout, register

# SET THE NAMESPACE!
app_name = 'inicio'

urlpatterns = [
	url(r'^$', index, name= 'index'),
	url(r'^logout/$', user_logout, name='user_logout'),
    url(r'^especial/',special, name='especial'),
    url(r'^registro/$', register, name = 'registro'),
    url(r'^login/$', user_login, name = 'user_login'),
]