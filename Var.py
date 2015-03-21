import os

class Var:
	def __init__(self, path):
		self.path = path
		self.name = path.split('/')[-1]

	def __str__(self):
		return self.name
