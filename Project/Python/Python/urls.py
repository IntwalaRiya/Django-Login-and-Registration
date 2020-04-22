from django.conf.urls import url
from django.urls import path
from register import views
from django.views.generic import TemplateView
from django.contrib import admin

app_name = 'Register' # So we can use it like: {% url 'mymodule:user_register' %} on our template.
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^user_home/$',views.user_home,name='user_home'),
    url(r'^$',views.user_register,name='user_register'),
    url('Register/', views.user_register, name='user_register'),
    url('Login/', views.user_login, name='user_login')
]
