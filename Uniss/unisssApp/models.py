from django.db import models

# Create your models here.
class estudiante(models.Model):

    nombre = models.CharField( max_length=50, verbose_name='Nombre')
    carnet_identidad = models.CharField( max_length=11, verbose_name='Ci')
    
    def __str__(self):
        return 'El nombre es: {}'.format(self.nombre) 
    
    
dict_agno = [
	('1', '1'),
	('2', '2'),
	('3', '3'),
	('4', '4'),
	('5', '5'),
    ]
class Disciplina(models.Model):
    idDisciplina = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30,)
    
    class Meta:
        verbose_name= 'Disciplina'
        verbose_name_plural= 'Disciplinas'
    
    def __str__(self):
     	return   self.nombre