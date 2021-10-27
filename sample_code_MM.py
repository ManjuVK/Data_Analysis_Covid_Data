#                               IMPORT LIBRARIES

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#                               READ DATASET
dataset = pd.read_csv("./WHO-COVID-19-global-data (1).csv")
Covid_cases = dataset['Cumulative_cases']
The_Untited_Kingdom = Covid_cases[132299:132926]
Italy = Covid_cases[64583:65210]
United_States_of_America = Covid_cases[141704:142331]

#*********************************************** TASK 1-3 ************************************************************
# Plot the data
x1 = np.arange(1,628)
y1 = The_Untited_Kingdom
y2 = Italy
y3 = United_States_of_America
plt.xticks(np.arange(1,628,50))
plt.xlim(xmin=0)
plt.xticks(rotation=0)
plt.xlabel("Days from begining of epidemic")
plt.ylabel("Number of Covid cases")
plt.title("Cumulative Covid cases of United Kingdom, Italy, USA from 03.01.2020 to 20.09.2021")
plt.plot(x1,y1,label='The Untited Kingdom', c='m')
plt.plot(x1,y2,label= 'Italy', c='y')
plt.plot(x1,y3,label= 'United States of America', c='c')
plt.legend()
plt.tight_layout()
plt.grid()
plt.show()

#******************************************* TASK 4 ***************************************************************
# Normalise data

normalised_United_Kingdom_dataset =  The_Untited_Kingdom[61:]/67886011
normalised_Italy_dataset = Italy[52:]/60461826
normalised_USA_dataset = United_States_of_America[52:]/331002651
# Normalised UK data
x1 = np.arange(1,567)
y1 = normalised_United_Kingdom_dataset
plt.xticks(np.arange(1,567,50))
plt.xlim(xmin=0)
plt.xticks(rotation=0)
plt.xlabel("Days from Cumulative cases = 100")
plt.ylabel("Number of Covid cases")
plt.title("Normalised Cumulative cases of United Kingdom from 04.03..2020 to 20.09.2021")
plt.plot(x1,y1,label='The Untited Kingdom', c='m')
plt.tight_layout()
plt.grid()
plt.show()
# Normalised USA & Italy
x1 = np.arange(1,576)
y1 = normalised_Italy_dataset
y2 = normalised_USA_dataset
plt.xticks(np.arange(1,576,50))
plt.xlim(xmin=0)
plt.xticks(rotation=0)
plt.xlabel("Days from Cumulative cases = 100")
plt.ylabel("Number of Covid cases")
plt.title("Normalised Cumulative cases of United States, Italy from 24.02.2020 to 20.09.2021")
plt.plot(x1,y1,label='Italy', c='c')
plt.plot(x1,y2,label='United States of America', c='y')
plt.tight_layout()
plt.grid()
plt.show()

#****************************************** TASK 5 *****************************************************************
# Taking log of normalised data
# UK
x1 = np.arange(1, 567)
log_Uk_dataset = np.log(normalised_United_Kingdom_dataset)
log_Uk_dataset = log_Uk_dataset.dropna()
y1 = log_Uk_dataset
UK_first_wave = y1[1:201]
UK_second_wave = y1[201:]
plt.xticks(np.arange(1,567,50))
plt.xlim(xmin=0)
plt.xticks(rotation=0)
plt.xlabel("Days from Cumulative cases = 100")
plt.ylabel("Cumulative Covid cases")
plt.title("Logarithmic graph for United Kingdom from 04.03.2020 to 20.09.2021")
plt.plot(x1,y1,label='The Untited Kingdom', c='y')
x1, y1 = [1.1, 37], [-12.65, -6.72]
plt.plot(x1, y1, '--g')
x1, y1 = [37, 70.5], [-6.72, -5.70]
plt.plot(x1, y1, '--r')
x1, y1 = [70.5, 201.6], [-5.70, -5.07]
plt.plot(x1, y1, '--g')
x1, y1 = [201.6,340.5 ], [-5.07, -2.81]
plt.plot(x1, y1, '--r')
x1, y1 = [340.5, 550.4], [-2.81, -2.32]
plt.plot(x1, y1, '--g')
plt.grid()
plt.show()
# first wave
x1 = np.arange(1,201)
y1 = UK_first_wave
plt.xticks(np.arange(1,201,50))
plt.ylabel("Number of Days")
plt.xlabel("Cumulative cases")
plt.title("First wave of UK")
plt.plot(x1, y1,label="UK First Wave", c="y")
x1, y1 = [0.8, 37], [-12.43, -6.67]
plt.plot(x1, y1, '--g')
x1, y1 = [37, 199], [-6.67, -5.11]
plt.plot(x1, y1, '--r')
plt.grid()
plt.show()
#finding slope and intercept
x1 = np.arange(1,38)
UK_firstsegment = UK_first_wave[1:38]
y1 = UK_firstsegment
UK_slope_intercept1 = np.polyfit(x1, y1, 1)
print("UK First wave- slope & intercept")
print(UK_slope_intercept1)
slope = 0.15483199
intercept = -11.70299942
UK_exp_model1 = np.exp(intercept + slope * x1)
y1 = UK_exp_model1
y2 = normalised_United_Kingdom_dataset[1:38]
y3 = y2 - y1
plt.title("Exponential growth of UK for first segment in Wave 1 ")
plt.xlabel("Days")
plt.ylabel("Number of cases")
plt.plot(x1, y1 ,label="Predicted wave",c="r")
plt.plot(x1, y2 ,label="Observed wave",c="b")
plt.plot(x1, y3, label = "Error", c="c")
plt.grid()
plt.legend()
plt.show()
#prediction for 1st UK wave
x1 = np.arange(1,201)
y1 = normalised_United_Kingdom_dataset[1:201]
UK_exp_model_firstwave = np.exp(intercept + slope * x1)
y1 = UK_exp_model_firstwave
y2 = normalised_United_Kingdom_dataset[1:201]
y3 = y2 - y1
plt.title("Exponential growth of UK for first Wave ")
plt.xlabel("Days")
plt.ylabel("Number of cases")
plt.plot(x1, y1 ,label="Predicted wave",c="r")
plt.plot(x1, y2 ,label="Observed wave",c="b")
plt.plot(x1, y3, label = "Error", c="c")
plt.grid()
plt.legend()
plt.show()
#second wave


