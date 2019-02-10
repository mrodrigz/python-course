from django import forms


class RepositorioBusqueda(forms.Form):

    ORDEN_CHOICES = (
        ('1', 'Fecha de creación'),
        ('2', 'Fecha de commit'),
    )

    ORDEN_DIR_CHOICES = (
        ('1', 'Ascendente'),
        ('2', 'Descendente'),
    )

    nombre = forms.CharField(required=False)
    orden = forms.CharField(widget=forms.Select(choices=ORDEN_CHOICES))
    direccion = forms.CharField(widget=forms.Select(choices=ORDEN_DIR_CHOICES))
