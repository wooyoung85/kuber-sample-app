from django.conf.urls import include, url
from . import views

app_name = 'api'
urlpatterns = [
    url(r'^analysis$', views.analysis, name='request-analysis'),
]