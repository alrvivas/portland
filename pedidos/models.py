#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill



class Template(models.Model):
	user = models.OneToOneField(User,null=True, blank=True)
	fecha_creacion = models.DateField(auto_now_add=True, blank=True)
	titulo_principal = models.CharField(max_length=100,null=True)
	color_titulo = models.CharField(max_length=25,null=True)
	iniciales = models.CharField(max_length=10,null=True)
	boton_1 = models.CharField(max_length=25,null=True)
	boton_2  = models.CharField(max_length=25,null=True)
	boton_3 = models.CharField(max_length=25,null=True)
	background = models.ImageField("Imagen Fondo", upload_to="images/background", blank=True, null=True,default='images/background/default-01.png')
	
	def __unicode__(self):
		return unicode(self.id)

	@models.permalink
	def get_absolute_url(self):
		return('template', (), { 'template_id': self.id })

class Pedido (models.Model):
	template = models.OneToOneField(Template,null=True, blank=True)
	costo = models.DecimalField(max_digits=4, decimal_places=2,blank=True,default=False)
	pagado = models.BooleanField(blank=True,default=False)

