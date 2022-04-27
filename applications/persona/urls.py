from django.urls import path, re_path, include

from . import views

app_name='persona_app'

urlpatterns = [
    path(
        'personas/',
        views.ListaPersonasListView.as_view(),
        name='personas'
    ),
    path(
        'api/persona/list',
        views.PersonasListAPIView.as_view()
    ),
    path(
        'api/persona/create',
        views.PersonaCreateView.as_view()
    ),
    path(
        'api/persona/detail/<pk>',
        views.PersonaRetrieveView.as_view(),
        name='detalle'
    ),
    path(
        'api/persona/delete/<pk>',
        views.PersonDeleteView.as_view()
    ),
    path(
        'api/persona/update/<pk>',
        views.PersonUpdateView.as_view()
    ),
    path(
        'api/persona/set/<pk>',
        views.PersonUpdateRetrieveView.as_view()
    ),
    path(
        'api/persons',
        views.Listado.as_view()
    ),
    path(
        'api/reuniones',
        views.ReunionApiLista.as_view()
    ),
    path(
        'api/reuniones-link',
        views.ReunionApiListaLink.as_view()
    ),
    path(
        'api/personas/paginacion/',
        views.PersonasPaginationAPIView.as_view()
    ),
    path(
        'api/reunion/job',
        views.ReunionByPersonJob.as_view()
    ),
]