from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^template/(?P<template_id>[-\w]+)$', 'pedidos.views.template', name='template'), 
	
)