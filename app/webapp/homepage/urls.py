__author__ = 'Patrick'
from django.conf.urls import url

from . import home
from django.conf import settings
from django.conf.urls.static import static
from homepage import views
from homepage.views import UserList
#

urlpatterns = [
    url(r'^$', home.index, name='index'),
    url(r'^2/$', home.index2, name='index2'),
    url(r'^3/$', UserList.as_view()),

    url(r'^users/$', views.user_list),
    url(r'^users/(?P<id>[0-9]+)/$', views.user_detail),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)