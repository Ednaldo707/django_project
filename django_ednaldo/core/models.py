# core/models.py

from django.db import models
from django.utils import timezone

# Status de escolha para o Evento
STATUS_CHOICES = (
    ('ABERTO', 'Aberto para Inscrição'),
    ('RESERVADO', 'Reservado/Lotado'),
    ('FINALIZADO', 'Evento Finalizado'),
)

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    data = models.DateField(default=timezone.now)
    horario = models.TimeField(default=timezone.now)
    descricao = models.TextField()
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='ABERTO'
    )
    
    # Propriedade para filtrar eventos futuros
    def is_futuro(self):
        return self.data >= timezone.now().date()

    def __str__(self):
        return self.titulo

class Projeto(models.Model):
    STATUS_CHOICES = (
        ('ATIVO', 'Ativo'),
        ('CONCLUIDO', 'Concluído'),
        ('ARQUIVADO', 'Arquivado'),
    )
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    # Adicionamos upload_to para organizar as imagens
    imagem_capa = models.ImageField(upload_to='projetos_capas/') 
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ATIVO')

    def __str__(self):
        return self.titulo

class Membro(models.Model):
    nome = models.CharField(max_length=150)
    cargo = models.CharField(max_length=100)
    # Adicionamos upload_to para organizar as fotos
    foto = models.ImageField(upload_to='membros_fotos/') 

    def __str__(self):
        return self.nome

class Midia(models.Model):
    TIPO_CHOICES = (
        ('IMAGEM', 'Imagem'),
        ('VIDEO', 'Vídeo'),
    )
    titulo = models.CharField(max_length=200)
    tipo_arquivo = models.CharField(max_length=6, choices=TIPO_CHOICES, default='IMAGEM')
    # O arquivo pode ser uma imagem ou um link (CharField para simplificar a URL de vídeo)
    arquivo = models.FileField(upload_to='midia_arquivos/', blank=True, null=True) 
    url_video = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titulo