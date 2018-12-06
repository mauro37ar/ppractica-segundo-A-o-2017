#!/usr/bin/python3

class Perro:
	def __init__(self,nombre,raza,color):
		self.nombre=nombre
		self.raza=raza
		self.color=color
	def bark (self):
		return  ("guau")

p=Perro("mauro","cocker","marron")
print (p)
print (p.bark())
