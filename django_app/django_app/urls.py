from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from analysis.views import AnalysisViewSet

router = routers.DefaultRouter()
router.register('analysis', AnalysisViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api/', include('api.urls')),
]
