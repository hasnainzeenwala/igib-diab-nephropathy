import form
import tkinter as tk
import pandas as pd
import select_params as sp
import graph as gpr

class Doctor:

	def truncate(self, n, decimals=0):
		multiplier = 10 ** decimals
		return int(n * multiplier) / multiplier

	def __init__(self):
		self.patients = []
		self.questions = {}
		self.filename='gene-list'

	def makeFullGraph(self):
		self.fullGraph = gpr.FullGraphProteins(self.questions.keys())

	def load_data(self):
		with open(self.filename, 'r') as gene_poly_names:
			for line in gene_poly_names:
				line = line.rstrip('\n')
				temp_list = line.split(',')
				self.questions[temp_list[0]]=temp_list[1:-1]
		self.makeFullGraph()
		scores_df = pd.read_csv('allele_score.csv')
		oddsrat_weight_df = pd.read_csv('allele_weight_oddsrat.csv')
		expoddsrat_weight_df = pd.read_csv('allele_weight_expoddsrat.csv')
		self.scores = scores_df.to_dict()
		self.oddsrat_weight = oddsrat_weight_df.to_dict()
		self.expoddsrat_weight = expoddsrat_weight_df.to_dict()

	def makeForm(self):
		self.load_data()
		self.doc_form = form.Form(self.questions)

	def getForm(self):
		return self.doc_form

	def geneWeight_to_allele(self, gene_weight_dict):
		w={}
		for gene in gene_weight_dict.keys():
			for allele in self.questions[gene]:
				w[gene + ' ' + allele] = gene_weight_dict[gene]
		return w


	def getMaxMinScore(self, selections, technique, scoreasked):
		allele_list=[]
		for selection in selections:
			for allele in self.questions[selection]:
				allele_list.append(selection+' ' + allele)
		curr_score = 0

		if(scoreasked=='max'):
			for allele in allele_list:
				if(technique == 'Odds Ratio Method'):
					if(self.scores[allele][0] == 1):
						curr_score += self.oddsrat_weight[allele][0]
				elif(technique == 'Exponential Odds Ratio Method'):
					if(self.scores[allele][0] == 1):
						curr_score += self.expoddsrat_weight[allele][0]

		elif(scoreasked=='min'):
			for allele in allele_list:
				if(technique == 'Odds Ratio Method'):
					if(self.scores[allele][0] == -1):
						curr_score -= self.oddsrat_weight[allele][0]
				elif(technique == 'Exponential Odds Ratio Method'):
					if(self.scores[allele][0] == -1):
						curr_score -= self.expoddsrat_weight[allele][0]

		return self.truncate(curr_score,1)



	def expodds_rat_Ana(self, selections):
		allele_list=[]
		for selection in selections:
			for allele in self.questions[selection]:
				allele_list.append(selection+' ' + allele)
		curr_score = 0
		for allele in allele_list:
			curr_score += self.patients[0].profile[allele][0] * self.scores[allele][0] *self.expoddsrat_weight[allele][0]
		return self.truncate(curr_score,1)

	def odds_rat_Ana(self, selections):
		allele_list=[]
		for selection in selections:
			for allele in self.questions[selection]:
				allele_list.append(selection+' ' + allele)
		curr_score = 0
		for allele in allele_list:
			curr_score += self.patients[0].profile[allele][0] * self.scores[allele][0] *self.oddsrat_weight[allele][0]
		return self.truncate(curr_score,1)

	def integ_Net_Ana(self, selections):
		w={}
		subgrph = self.fullGraph.get_subGraph(selections)
		for selection in selections:
			w[selection] = 1+subgrph.get_all_edge_weights(selection)
		w_allele = self.geneWeight_to_allele(w)
		curr_score = 0
		for allele in w_allele.keys():
			curr_score += self.patients[0].profile[allele][0] * w_allele[allele]*self.scores[allele][0] #* self.score_table[allele][0]
		return self.truncate(curr_score,1)

	def analyseResponse(self, patient):
		root = tk.Tk()

		#excluding those genes that patient has marked as 'other'
		genes_for_analysis = []
		for gene in self.questions.keys():
			if(self.patients[0].profile[gene + ' ' + 'other'][0] != 1):
				genes_for_analysis.append(gene)

		doctor_checkbox = sp.Doctor_Checkbox(self, genes_for_analysis, root, ['Odds Ratio Method', 'Exponential Odds Ratio Method', 'Network Analysis'])
		doctor_checkbox.pack(side="top", fill="both", expand=True)
		

		root.mainloop()


	def addPatient(self, patient):
		self.patients.append(patient)