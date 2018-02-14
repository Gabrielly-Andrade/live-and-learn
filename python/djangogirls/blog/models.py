from django.db import models
from django.utils import timezone

class Post(models.Model): # models.Model indica que o Post deve ser salvo em um banco de dados
    author = models.ForeignKey('auth.User') # Link para outro modelo
    title = models.CharField(max_length=200) # Limita o número de caracteres com a propriedade "CharField"
    text = models.TextField() # Propriede sem limite de texto
    created_date = models.DateTimeField( # Propriedade que define data e hora
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self): # Dunder (double-underscore)
        return self.title
