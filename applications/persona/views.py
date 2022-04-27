from django.shortcuts import render

from django.views.generic import ListView

from .serializers import ( PersonSerializer, 
PersonaSerializer, 
ReunionSerializer, 
PersonaSerializer3,
ReunionSerializer2,
ReunionSerializerLink,
PersonPagination,
CountReounionSerializer
) #Importar serializables

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView
) #Importar framework de API

from .models import Person, Reunion

#Uso de templates html
class ListaPersonasListView(ListView):
    template_name = "persona/lista.html"
    context_object_name = 'personas'

    def get_queryset(self):
        return Person.objects.all()

"""API Rest"""
  
#Listar
class PersonasListAPIView(ListAPIView):

    #Indicar serializable, Serializar- Convertir a JSON
    serializer_class = PersonSerializer

    #Recuperar objetos por medio de ORM
    def get_queryset(self):
        return Person.objects.all()

#Crear
class PersonaCreateView(CreateAPIView):

    serializer_class = PersonSerializer

#Detalle, muestra toda la info de un elemento con su id
class PersonaRetrieveView(RetrieveAPIView):

    serializer_class = PersonSerializer
    queryset = Person.objects.all()

#Eliminar
class PersonDeleteView(DestroyAPIView):

    queryset = Person.objects.all()
    serializer_class = PersonSerializer

#Actualizar
class PersonUpdateView(UpdateAPIView):

    queryset = Person.objects.all()
    serializer_class = PersonSerializer

#Detalle + Actualizar, trae los datos y actualiza
class PersonUpdateRetrieveView(RetrieveUpdateAPIView):
    
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class Listado(ListAPIView):
    """
        Vista para interactuar con serializadores
    """
    serializer_class = PersonaSerializer3

    def get_queryset(self):
        return Person.objects.all()

#Uso de link, para no traer toda la info, mostrar en un link info de llave foranea
class ReunionApiListaLink(ListAPIView):
 
    serializer_class = ReunionSerializerLink

    def get_queryset(self):
        return Reunion.objects.all()

#Uso de llaves foraneas
class ReunionApiLista(ListAPIView):
     
    serializer_class = ReunionSerializer

    def get_queryset(self):
        return Reunion.objects.all()

#Paginacion
class PersonasPaginationAPIView(ListAPIView):
    
    serializer_class = PersonSerializer
    pagination_class = PersonPagination

    def get_queryset(self):
        return Person.objects.all()

#Uso de Managers, es necesario especificar un serializer
class ReunionByPersonJob(ListAPIView):
    serializer_class = CountReounionSerializer

    def get_queryset(self):
        return Reunion.objects.cantidad_reuniones_job()