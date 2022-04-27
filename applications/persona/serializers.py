from applications.persona.models import Person
from rest_framework import serializers, pagination
from .models import Hobby, Person, Reunion

#Creacion de serializables por modelo
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person #Indicar modelo, importarlo
        #Asignar campos que devolvera el JSON
        fields = (
            'id',
            'full_name',
            'job',
            'email',
            'phone',
            'hobbies'
        )

#Serializable personalizado
class PersonaSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    job = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    activo = serializers.BooleanField(default=False)

#Traer toda la info de hobbies
class HobbySerializer(serializers.ModelSerializer):

    class Meta:
        model = Hobby
        fields = ('__all__')

#Uso de relacion muchos a muchos
class PersonaSerializer3(serializers.ModelSerializer):

    hobbies = HobbySerializer(many=True)

    class Meta:
        model = Person
        fields = (
            'id',
            'full_name',
            'job',
            'email',
            'phone',
            'hobbies'
        )

#Con info de llaves foranea uno a mucho
class ReunionSerializer(serializers.ModelSerializer):
    
    persona = PersonaSerializer()

    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona'  
        )

#Metodos en Serializador, realizar cualquier operacion y mostrarla en el Serializer en el Json
class ReunionSerializer2(serializers.ModelSerializer):

    fecha_hora = serializers.SerializerMethodField()

    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona',
            'fecha_hora'
        )

    def get_fecha_hora(self, obj):
        return str(obj.fecha) + ' - '+str(obj.hora)

#Mostrar info de llave foranea en un nuevo link
class ReunionSerializerLink(serializers.HyperlinkedModelSerializer): 

    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona'
        )
        extra_kwargs = {
            'persona':{'view_name':'persona_app:detalle','lookup_field':'pk'}
        }

#Serializable de paginacion
class PersonPagination(pagination.PageNumberPagination):
    page_size = 2
    max_page_size = 100

#Serializador personalizado
class CountReounionSerializer(serializers.Serializer):
    persona__job = serializers.CharField()
    cantidad = serializers.IntegerField()
