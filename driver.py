import doctor as doc 
import patient as pat
import form as fr

doc1 = doc.Doctor()
doc1.makeForm()

pat1 = pat.Patient()
pat1.fillForm(doc1.doc_form)


doc1.addPatient(pat1)

doc1.analyseResponse(pat1)

