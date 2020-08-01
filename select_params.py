import windows_with_scroll_bar as wwsb
import tkinter as tk
class Doctor_Checkbox(wwsb.Windw):
	def __init__(self, doctor, params, root, techniques):
		self.params = params
		self.dropdown = techniques
		self.selections=[] 
		self.doctor=doctor
		super().__init__(root, 500, 500)
		

	def populate(self):
		i=1
		j=0
		scoreText = tk.StringVar()
		optn_selected = tk.StringVar()
		for param in self.params:
			self.selections.append(tk.StringVar())
			self.selections[j].set(0)
			tk.Checkbutton(self.frame, text=param, onvalue=param, offvalue=0, variable=self.selections[j],
				font=('Courier', 20), command=lambda: self.return_listOfSelections(scoreText, optn_selected, max_score, min_score)).grid(row=i, column=0, sticky=tk.W)
			j+=1
			i+=2
		i+=1
		
		optn_selected.set(self.dropdown[0])
		optn_selected.trace("w", lambda arg1,arg2,arg3: self.return_listOfSelections(scoreText, optn_selected, max_score, min_score))
		tk.OptionMenu(self.frame, optn_selected, *self.dropdown).grid(row=i, column=0)
		i+=1
		score = tk.Label(self.frame, text="Score: ", font=('Courier',20))
		score.grid(row=i, column=0)
		scoreValue = tk.Label(self.frame, textvariable=scoreText, font=('Courier', 20))
		scoreValue.grid(row=i, column=1)
		i=i+1
		max_score = tk.StringVar()
		tk.Label(self.frame, text= "Max Score: ", font=('Courier', 20)).grid(row=i, column=0)
		tk.Label(self.frame, textvariable=max_score, font=('Courier', 20)).grid(row=i, column=1)
		
		i += 1
		min_score = tk.StringVar()
		tk.Label(self.frame, text="Min Score: ", font=('Courier', 20)).grid(row=i, column=0)		
		tk.Label(self.frame, textvariable=min_score, font=('Courier', 20)).grid(row=i, column=1)

	def return_listOfSelections(self, scoreText, optn_selected, max_score, min_score):
		selection_string_list=[]
		for selection in self.selections:
			if(selection.get() != '0'):
				selection_string_list.append(selection.get())

		max_score.set(str(self.doctor.getMaxMinScore(selection_string_list, optn_selected.get(), 'max')))
		min_score.set(str(self.doctor.getMaxMinScore(selection_string_list, optn_selected.get(), 'min')))

		if(optn_selected.get() == 'Network Analysis'):
			scoreText.set(str(self.doctor.integ_Net_Ana(selection_string_list)))


		elif(optn_selected.get() == 'Odds Ratio Method'):
			scoreText.set(str(self.doctor.odds_rat_Ana(selection_string_list)))



		elif(optn_selected.get() == 'Exponential Odds Ratio Method'):
			scoreText.set(str(self.doctor.expodds_rat_Ana(selection_string_list)))


# if __name__ == "__main__":
# 	params=['mera', 'joota', 'hai', 'japani']
# 	tech = ['bill gates', 'steve jobs']
# 	root=tk.Tk()
# 	example = Doctor_Checkbox(params, root, tech)
# 	example.pack(side="top", fill="both", expand=True)

# 	root.mainloop()

