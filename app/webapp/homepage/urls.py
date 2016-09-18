__author__ = 'Patrick'
from django.conf.urls import url

from . import home
from django.conf import settings
from django.conf.urls.static import static
from homepage import views
from homepage.views import BabyList
#

urlpatterns = [
    url(r'^$', home.index, name='index'),
    # url(r'^2/$', home.index2, name='index2'),

    url(r'^api/v1/babies/$', BabyList.as_view()),    #GET to return baby list, POST to create new baby
    # url(r'^api/v1/daddies/$', DaddyList.as_view()),    #GET to return daddy list, POST to create new daddy
    url(r'^api/v1/babies/new$', views.baby_list),    #GET to return baby list, POST to create new baby

    url(r'^api/v1/babies/all/$', views.baby_list),  #GET to return of baby list in JSON format
    url(r'^api/v1/babies/(?P<id>[0-9]+)/$', views.baby_detail),  #GET to return specific baby info in JSON format, POST to update baby info

    url(r'^api/v1/daddies/all/$', views.daddy_list),  #GET to return of baby list in JSON format
    url(r'^api/v1/daddies/(?P<id>[0-9]+)/$', views.daddy_detail),  #GET to return specific daddy info, POST to update daddy info

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)