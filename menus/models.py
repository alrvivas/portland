from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill



class Cliente(models.Model):
	user = models.OneToOneField(User,null=True, blank=True)
	fecha_ingreso = models.DateField(null=True)
	direccion = models.CharField(max_length=140,null=True)
	
