import os

class IntLit:
	def __init__(self, path):
		self.path = path
		self.val = int(path.split('/')[-1])

	def __str__(self):
		return str(self.val)
