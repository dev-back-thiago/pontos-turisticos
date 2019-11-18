from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from core.models import PontosTuristicos
from .serializers import PontosTuristicosSerializer
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions


class PontosTuristicosViewSet(ModelViewSet):

    serializer_class = PontosTuristicosSerializer
    filter_backends = [SearchFilter]
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    search_fields = ('id','nome', 'descricao', 'endereco__linha1')
    lookup_field: str = 'nome'
    lookup_field: str = 'id'


    def get_queryset(self):
        return PontosTuristicos.objects.filter(aprovado=True)