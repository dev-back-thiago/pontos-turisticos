from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from atracoes.models import Atracao
from core.models import PontosTuristicos
from atracoes.api.serializers import AtracaoSerializer
from endereco.api.serializers import EnderecoSerializer


class PontosTuristicosSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True, read_only=True)
    endereco = EnderecoSerializer(read_only=True)
    descricao_completa = SerializerMethodField()
    class Meta:
        model = PontosTuristicos
        fields = ('id', 'nome', 'descricao', 'aprovado',
                  'foto', 'atracoes', 'comentarios', 'avaliacoes', 'endereco', 'descricao_completa', 'descricao_completa2')


        read_only_fields = ('comentarios', 'avaliacoes')

    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)

    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']
        ponto = PontosTuristicos.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto)
        return ponto

    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)