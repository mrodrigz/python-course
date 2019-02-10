from django.db import models
import datetime


class ConsultaAPI(models.Model):

    fecha = models.DateTimeField()


class Repositorio(models.Model):

    nombre = models.CharField(max_length=200)

    fechaCreacion = models.DateTimeField(default=None)

    fechaCommit = models.DateTimeField(default=None)

    consultaApi = models.ForeignKey(
        ConsultaAPI,
        default=None,
        on_delete=models.CASCADE
    )
