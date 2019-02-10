from django.conf.urls import url
from miapppy import views

urlpatterns = [
    url(r'^$', views.root),
    url(r'^hello/$', views.hello),
    url(r'^busqueda/$', views.RepositorioBusquedaView.as_view()),
    # url(r'^ordenar/$', views.RepositorioOrdenadoView.as_view()),
    url(r'^filtrar/$', views.RepositorioFiltradoView.as_view()),
]
