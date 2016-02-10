#encoding:utf-8
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.files.images import get_image_dimensions
from .models import Template

class pedidoForm(ModelForm):

	class Meta:
		model = Template
		fields = '__all__'

