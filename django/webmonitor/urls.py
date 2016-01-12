from django.conf.urls import url

from . import views

from webmonitor import views

#API REST
router = routers.DefaultRouter()

router.register(r'api/v1/registros/(?P<sensor_id>\d+)', views.RegistrosViewSet,"sensor_id")
router.register(r'api/v1/registros', views.RegistrosViewSet,"sensor_id")

router.register(r'api/v1/related', views.RelacionesViewSet,"sensor_id")

router.register(r'api/v1/sensors', views.SensoresViewSet,"sensor_id")

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.index, name='index'),
    url(r'^dashboard\.html$', views.dashboard, name='dashboard'),
    url(r'^dashboard$', views.index, name='index'),

    url(r'^graficas\.html$', views.graficas, name='graficas'),
    url(r'^graficas$', views.index, name='index'),

    #API Rest
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]