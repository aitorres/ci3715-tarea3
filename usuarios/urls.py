from django.conf.urls import url, include
from .views import login, register, perfil, logout

urlpatterns = [
    url(r'^$', login),
    url(r'^register/', register),
    url(r'^logout/', logout),
    url(r'^perfil/$',  perfil),
]