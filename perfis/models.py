from django.db import models

class Perfil(models.Model):

    nome = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    telefone = models.CharField(max_length=15, null=False)
    nome_empresa = models.CharField(max_length=255, null=False)

    @staticmethod
    def convidar(request, perfil_convidado):
        Convite(solicitante=Perfil.get_perfil_logado(request), convidado=perfil_convidado).save()

    @staticmethod
    def get_perfil_logado(request):
        return Perfil.objects.get(id=2)

class Convite(models.Model):

    solicitante = models.ForeignKey(Perfil, related_name='convites_feitos')
    convidado = models.ForeignKey(Perfil, related_name='convites_recebidos')
