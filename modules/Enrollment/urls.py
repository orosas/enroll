from django.conf.urls import url
from .views import Index, Login

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #url(r'^(?P<error>[\w-]+)$', Index, name='index-disclaimer'),
    url(r'^$', Index, name='index'),
    url(r'^login$', Login, name='login'),
    #url(r'^region/(?P<region>[\w-]+)/$', lista_Sitiosxregion, name='sitios_por_region'),
    #url(r'^busqueda/$', Busqueda_Sitio, name='busqueda_sitio'),
    #url(r'^detallesitio/(?P<pk>\d+)/$', Detalle_Sitio, name='detalle_sitio'),
]