import pandas as pd
import math

## This script isn't a part of the main program, and it needn't be run. It was only run once to generate weights and store them in the csv files 

def weight_malign(oddsr, min_rat, max_rat):
	return oddsr - 0.45*(max_rat-min_rat)

def weight_protec(oddsr, min_rat, max_rat):
	return 2-oddsr-0.45*(max_rat-min_rat)

allele_weight = {}
allele_weight["APOE E2/3/4 (E2)"] = [weight_malign(1.7, 1.12, 2.58)]
allele_weight["APOE E2/3/4 (E4)"] = [weight_protec(0.78, 0.62, 0.98)]
allele_weight["APOE other"] = [0]
allele_weight["APOC1 rs4420638 (G)"] = [weight_malign(1.54, 1.29, 1.83)]
allele_weight["APOC1 other"] = [0]
allele_weight["GREM1 rs1129456 (T)"] = [weight_malign(1.53, 1.25, 1.89)]
allele_weight["GREM1 other"] = [0]
allele_weight["AKR1B1 rs759853 (T)"] = [weight_malign(1.40, 1.13, 1.74)]
allele_weight["AKR1B1 CA repeat (Z-2)"] = [weight_malign(1.12, 1.02, 1.24)]
allele_weight["AKR1B1 other"] = [0]
allele_weight["NOS3 rs2070744 (C)"] = [weight_malign(1.39, 1.09, 1.78)]
allele_weight["NOS3 rs3138808 (a)"] = [weight_malign(1.31, 1.02, 1.67)]
allele_weight["NOS3 other"] = [0]
allele_weight["CARS rs739401 (C)"] = [weight_malign(1.32, 1.15, 1.51)]
allele_weight["CARS rs451041 (A)"] = [weight_malign(1.37, 1.21, 1.54)]
allele_weight["CARS other"] = [0]
allele_weight["ACE rs179975 (D)"] = [weight_malign(1.24, 1.12, 1.37)]
allele_weight["ACE other"] = [0]
allele_weight["UNC13B rs13293564 (T)"] = [weight_malign(1.23, 1.11, 1.35)]
allele_weight["UNC13B other"] = [0]
allele_weight["FRMD3 rs1888747 (C)"] = [weight_protec(0.74, 0.65, 0.83)]
allele_weight["FRMD3 rs10868025 (A)"] = [weight_protec(0.72, 0.64, 0.81)]
allele_weight["FRMD3 other"] = [0]
allele_weight["HSPG2 rs3767140 (G)"] = [weight_protec(0.72, 0.59, 0.87)]
allele_weight["HSPG2 other"] = [0]
allele_weight["EPO rs1617640 (T)"] = [weight_protec(0.67, 0.6, 0.76)]
allele_weight["EPO other"] = [0]
allele_weight["VEGFA rs833061 (C)"] = [weight_protec(0.48, 0.37, 0.61)]
allele_weight["VEGFA other"] = [0]
allele_weight["CPVL rs39059 (G)"] = [weight_protec(0.74, 0.64, 0.85)]
allele_weight["CPVL other"] = [0]

allele_score = {}
allele_score["APOE E2/3/4 (E2)"] = [1]
allele_score["APOE E2/3/4 (E4)"] = [-1]
allele_score["APOE other"] = [0]
allele_score["APOC1 rs4420638 (G)"] = [1]
allele_score["APOC1 other"] = [0]
allele_score["GREM1 rs1129456 (T)"] = [1]
allele_score["GREM1 other"] = [0]
allele_score["AKR1B1 rs759853 (T)"] = [1]
allele_score["AKR1B1 other"] = [0]
allele_score["AKR1B1 CA repeat (Z-2)"] = [1]
allele_score["NOS3 rs2070744 (C)"] = [1]
allele_score["NOS3 rs3138808 (a)"] = [1]
allele_score["NOS3 other"] = [0]
allele_score["CARS rs739401 (C)"] = [1]
allele_score["CARS rs451041 (A)"] = [1]
allele_score["CARS other"] = [0]
allele_score["ACE rs179975 (D)"] = [1]
allele_score["ACE other"] = [0]
allele_score["UNC13B rs13293564 (T)"] = [1]
allele_score["UNC13B other"] = [0]
allele_score["FRMD3 rs1888747 (C)"] = [-1]
allele_score["FRMD3 rs10868025 (A)"] = [-1]
allele_score["FRMD3 other"] = [0]
allele_score["HSPG2 rs3767140 (G)"] = [-1]
allele_score["HSPG2 other"] = [0]
allele_score["EPO rs1617640 (T)"] = [-1]
allele_score["EPO other"] = [0]
allele_score["VEGFA rs833061 (C)"] = [-1]
allele_score["VEGFA other"] = [0]
allele_score["CPVL rs39059 (G)"] = [-1]
allele_score["CPVL other"] = [0]

df_allele_weight_oddrat = pd.DataFrame.from_dict(allele_weight)

df_allele_score = pd.DataFrame.from_dict(allele_score)

df_allele_weight_oddrat.to_csv('allele_weight_oddsrat.csv')
df_allele_score.to_csv('allele_score.csv')

allele_weight_log = {}
for key in allele_weight.keys():
	allele_weight_log[key] = [math.exp(allele_weight[key][0])]

df_allele_weight_logoddrat = pd.DataFrame.from_dict(allele_weight_log)
df_allele_weight_logoddrat.to_csv('allele_weight_expoddsrat.csv')


