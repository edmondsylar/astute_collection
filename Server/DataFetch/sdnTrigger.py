from .sdnContainer import *

class sdn_trigger:
	def __init__(self, file, batch):
		self.file = file
		self.batch = batch

		container(self.file, self.batch)
