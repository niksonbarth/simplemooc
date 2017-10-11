from django.conf.urls import include, url
from django.contrib.auth import views as auth
from simplemooc.accounts import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^entrar/$', auth.login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^sair/$', auth.logout, {'next_page': 'core:home'}, name='logout'),
    url(r'^cadastre-se/$', views.register, name='register'),
    url(r'^editar/$', views.edit, name='edit'),
    url(r'^editar-senha/$', views.edit_password, name='edit_password'),
    url(r'^nova-senha/$', views.password_reset, name='password_reset'),
    url(r'^confirmar-nova-senha/(?P<key>\w+)/$', views.password_reset_confirm, name='password_reset_confirm'),
]
