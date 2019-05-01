from django.db import models

class Name(models.Model):
	nome = models.CharField(max_length=80)
	telefone = models.CharField(max_length=22)
	email = models.TextField()
	
	def __str__(self):
		return self.nome
