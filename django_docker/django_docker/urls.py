from django.conf.urls import include, url
from hello_world.views import hello_world
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', hello_world, name='home'),
    #url(r'^$', 'hello_world.views.hello_world', name='hello_world'),
]
