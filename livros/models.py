from django.db import models

# Create your models here.

class Livros(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=400)
    editora = models.CharField(max_length=200)
    quantidade = models.IntegerField()
    data_cadastro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
<<<<<<< HEAD
        return self.nome
=======
        return self.editora

    class Meta:
        verbose_name_plural = 'Livros'
        
>>>>>>> 5e51ac3 (Master 2.3)
