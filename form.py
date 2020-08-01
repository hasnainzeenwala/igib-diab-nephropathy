import tkinter as tk
import pandas as pd

class Form:
	def __init__(self, questions):
		self.questions = questions
		self.responses={}

	@staticmethod
	def onFrameConfigure(canvas):
		canvas.configure(scrollregion=canvas.bbox("all"))


	def showForm(self):

		HEIGHT = 800
		WIDTH = 800

		self.root = tk.Tk()
		canvas = tk.Canvas(self.root, height=HEIGHT, width=WIDTH, background="#ffffff")
		questions_frame = tk.Frame(canvas, background="#ffffff")
		vsb = tk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
		canvas.configure(yscrollcommand=vsb.set)

		vsb.pack(side="right", fill="y")
		canvas.pack(side="left", fill="both", expand=True)
		canvas.create_window((4,4), window=questions_frame, anchor="nw")

		questions_frame.bind("<Configure>", lambda event, canvas=canvas: Form.onFrameConfigure(canvas))

		gene_allele = []
		for i in range(len(self.questions.keys())):
			gene_allele.append(tk.StringVar())
			gene_allele[i].set('other')

		i=0
		row=0
		
		tk.Label(questions_frame, text="Diabetic Nephropathy Form", font=('Helvetica', 20)).grid(row=row, column=0)

		row += 1
		for gene in self.questions.keys():
			ques_label = tk.Label(questions_frame, text = "Which polyporphism of the " + gene + " gene does the patient have:", font=('Courier', 20))
			ques_label.grid(row=row,column=0)
			row+=1
			for allele in self.questions[gene]:
				R1 = tk.Radiobutton(questions_frame, text=allele, variable=gene_allele[i], value=allele)
				R1.grid(row=row,column=0, sticky=tk.W)
				row+=1
			row+=1
			i=i+1
		submit_button = tk.Button(questions_frame, text="Submit", bg='red', command=lambda: self.getEntry(gene_allele), font=('Helvetica', 20))
		submit_button.grid(row=row+5, column = 0)



		self.root.mainloop()


	def getEntry(self, gene_allele):
		i=0
		for gene in self.questions.keys():
			for allele in self.questions[gene]:
				if(allele == gene_allele[i].get()):
					self.responses[gene + ' ' + allele] = [1]
				else:
					self.responses[gene + ' ' + allele] = [0]

			i += 1
		df_forpat = pd.DataFrame(self.responses)
		df_forpat.to_csv('patientdata.csv')

		self.root.destroy()

