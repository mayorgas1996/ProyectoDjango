from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.CharField(max_length=255, verbose_name='Descripción')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
    
    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=159, verbose_name='Titulo')
    content = RichTextField(verbose_name='Contenido')
    image = models.ImageField(default='null', verbose_name='Imagen')
    public = models.BooleanField(verbose_name="¿Publicado?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha modificación")
    
    #Relación 1 a 1 -> Un articulo pertenece a un Usuario
    user = models.ForeignKey(User, verbose_name = "Usuario", on_delete=models.CASCADE) 
    #Relación muchos a muchos -> muchos articulos pueden tener muchas categorías
    category = models.ManyToManyField(Category, verbose_name='Categorías', blank=True) 

    class Meta:
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'
    
    def __str__(self):
        return self.title