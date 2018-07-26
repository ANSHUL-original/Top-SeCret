from django.conf.urls import url
from .views import about,home,contactus,single,posts,delete_v,edit


#login views import
from .views import login_v,logout_v,register

#website urls
from .views import arun,contact,index,trip,confirm


urlpatterns = [
    url(r'^arun/$',arun,name='arun'),
    url(r'^contact/$',contact,name='contact'),
    url(r'^index/$',index,name='index'),
    url(r'^trip/$',trip,name='trip'),
    url(r'^confirm/$', confirm,name='confirm'), 




	url(r'^register/$', register, name='register'),
	url(r'^logout/$', logout_v, name='logout_v'),
	

	url(r'^single/(?P<id>\d+)/$',single,name='single'),
	url(r'^edit/(?P<id>\d+)/$',edit,name='edit'),
    url(r'^delete/(?P<id>\d+)/$',delete_v,name='delete_v'),
    url(r'^posts/$',posts,name='posts'),
    url(r'^about/$', about, name='about'),
    url(r'^contactus/$', contactus, name='contactus'),
    url(r'^home/$', home, name='home'),

    url(r'^$', login_v, name='login_v')
]