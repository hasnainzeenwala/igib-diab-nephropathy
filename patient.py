import form as fm
import pandas as pd

class Patient:

	def __init(self):
		self.profile={}

	def fillForm(self, form):
		form.showForm()
		self.profile = form.responses
	def getResponses(self):
		return self.profile