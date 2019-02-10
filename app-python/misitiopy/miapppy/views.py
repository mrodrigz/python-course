from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.shortcuts import render
from miapppy.forms import RepositorioBusqueda
from miapppy.models import ConsultaAPI
from miapppy.models import Repositorio
import requests
import datetime
from django.template.loader import get_template
# from apps.testapp.models import Developer


def root(request):
    # assert False  # Sirve para romper el flujo
    return HttpResponse('Mi aplicación')


def hello(request):
    # r = requests.get('https://api.github.com/orgs/githubtraining/repos')
    return HttpResponse('Hello World!')

"""
def filtrar_repositorio(request, nombre):
    # verificando si tiene dato el parámetro
    if nombre != None and nombre != '':
        repos = Repositorio.objects.filter(nombre__contains=nombre)
    else:
        repos = Repositorio.objects.all()

    # retornando el listado
    return repos
"""

def filtrar_repositorio(request, nombre, orden, direccion):

    # analizando la direccion
    dir = ''
    if direccion == '2':
        dir = '-'

    # definiendo el orden
    if orden == '1':
        if nombre == None or nombre == '':
            order_repos = Repositorio.objects.order_by(dir + 'fechaCreacion')
        else:
            order_repos = Repositorio.objects.filter(nombre__contains=nombre).order_by(dir + 'fechaCreacion')
    else:
        if nombre == None or nombre == '':
            order_repos = Repositorio.objects.order_by(dir + 'fechaCommit')
        else:
            order_repos = Repositorio.objects.filter(nombre__contains=nombre).order_by(dir + 'fechaCommit')

    print('nombre = {}, orden = {}, direccion = {} '.format(nombre, orden, direccion))
    # retornando la lista ordenada
    return order_repos


def consultar_repositorio_all(request):

    # consultando en la base de datos si existe información de repositorios
    all_repos = Repositorio.objects.all()

    # verificando si tiene info
    if len(all_repos) == 0:
        # consultando el rest
        lista = requests.get('https://api.github.com/orgs/githubtraining/repos')
        items = lista.json()

        # registrando una consulta nueva
        consulta = ConsultaAPI(fecha=datetime.datetime.now())
        consulta.save()

        # contador
        cant = 0

        # recorriendo el contenido del json
        for item in items:
            # obteniendo los datos
            nom_repo = item["name"]
            fec_cre_repo = item["created_at"]
            fec_cmm_repo = item["pushed_at"]

            # creando un objeto
            repo = Repositorio(nombre=nom_repo,fechaCreacion=fec_cre_repo,fechaCommit=fec_cmm_repo,consultaApi=consulta)
            repo.save()
            cant += 1
            if cant == 10:
                # saliendo del bucle
                break

        # retornando el resultado
        repos = Repositorio.objects.filter(consultaApi=consulta)
        return repos
        # context = {'repos': repos}
        # return render(request, 'miapppy/busqueda.html', context)
        # return HttpResponse('Hello World!')

    # si no ingresa a la condición, retornamos la lista general
    return all_repos


class RepositorioBusquedaView(TemplateView):

    # colocando el nombre al template
    template_name = 'miapppy/busqueda.html'

    def get(self, request, *args, **kwargs):
        form = RepositorioBusqueda()

        # consultando el repositorio
        repos = consultar_repositorio_all(request)

        return self.render_to_response({'form': form, 'repos': repos})

    def post(self, request, *args, **kwargs):
        form = RepositorioBusqueda(request.POST)
        # if not form.is_valid():
        #    return self.render_to_response({'form': form})

        # obteniendo la variable
        # nombre = request.POST.get('nombre')
        # return HttpResponse('El valor buscado es: {}'.format(nombre))

        # consultando el repositorio
        repos = consultar_repositorio_all(request)

        return self.render_to_response({'form': form, 'repos': repos})


class RepositorioFiltradoView(TemplateView):

    # colocando el nombre al template
    template_name = 'miapppy/busqueda.html'

    def get(self, request, *args, **kwargs):
        form = RepositorioBusqueda()

        # obteniendo las variables
        nombre = request.GET.get('nombre')
        orden = request.GET.get('orden')
        direccion = request.GET.get('direccion')

        print('GET -- nombre = {}, orden = {}, direccion = {} '.format(nombre, orden, direccion))

        # consultando el repositorio
        repos = filtrar_repositorio(request, nombre=nombre, orden=orden, direccion=direccion)

        return self.render_to_response({'form': form, 'repos': repos})

    def post(self, request, *args, **kwargs):
        form = RepositorioBusqueda(request.POST)
        # if not form.is_valid():
        #     return self.render_to_response({'form': form})

        # obteniendo las variables
        nombre = request.POST.get('nombre')
        orden = request.POST.get('orden')
        direccion = request.POST.get('direccion')

        print('POST -- nombre = {}, orden = {}, direccion = {} '.format(nombre, orden, direccion))

        # consultando el repositorio
        repos = filtrar_repositorio(request, nombre=nombre, orden=orden, direccion=direccion)

        return self.render_to_response({'form': form, 'repos': repos})

"""
class RepositorioFiltradoView(TemplateView):

    # colocando el nombre al template
    template_name = 'miapppy/busqueda.html'

    def get(self, request, *args, **kwargs):
        form = RepositorioBusqueda()

        # obteniendo las variables
        nombre = request.GET.get('nombre')

        # consultando el repositorio
        repos = filtrar_repositorio(request, nombre=nombre)

        return self.render_to_response({'form': form, 'repos': repos})

    def post(self, request, *args, **kwargs):
        form = RepositorioBusqueda(request.POST)
        # if not form.is_valid():
        #    return self.render_to_response({'form': form})

        # obteniendo las variables
        nombre = request.POST.get('nombre')

        # consultando el repositorio
        repos = filtrar_repositorio(request, nombre=nombre)

        return self.render_to_response({'form': form, 'repos': repos})
"""
