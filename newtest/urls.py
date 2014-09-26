from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'newtest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'newtest.helloworld.index'),
	url(r'^add/$', 'newtest.add.index'),
	url(r'^list/$', 'newtest.list.index'),
]
