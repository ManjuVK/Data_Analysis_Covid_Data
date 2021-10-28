#                               IMPORT LIBRARIES

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#                               READ DATASET
dataset = pd.read_csv("./WHO-COVID-19-global-data (1).csv")
Covid_cases = dataset['Cumulative_cases']
United_States_of_America = Covid_cases[141704:142331]
normalised_USA_dataset = United_States_of_America[52:]/331002651
#*************************** Plot log_data
x1 = np.arange(1,576)
log_USA_dataset = np.log(normalised_USA_dataset)
log_USA_dataset = log_USA_dataset.dropna()
y1 = log_USA_dataset
USA_first_wave = y1[1:232]
USA_second_wave = y1[233:576]
plt.xticks(np.arange(1,576,50))
plt.xlim(xmin=0)
plt.xticks(rotation=0)
plt.xlabel("Days from Cumulative cases = 100")
plt.ylabel("Cumulative Covid cases ")
plt.title("Logarithmic graph for United States of America from 24.02.2020 to 20.09.2021")
plt.plot(x1,y1,label='United States of America', c='y')
#first wave
x1, y1 = [1.1, 57.2], [-14.97, -6.09]
plt.plot(x1, y1, '--g')
x1, y1 = [57.2, 232.7], [-6.09, -3.76]
plt.plot(x1, y1, '--r')
#second wave
x1, y1 = [232.7, 349.9], [-3.76, -2.47]
plt.plot(x1, y1, '--g')
x1, y1 = [349.9, 550.4], [-2.47, -2.17]
plt.plot(x1, y1, '--r')
plt.grid()
plt.show()
#********************************************** USA First WAVE *****************************************************
y1 = USA_first_wave
x1 = np.arange(1, 232)
plt.xticks(np.arange(1,232,50))
plt.xlim(xmin=0)
plt.xticks(rotation=0)
plt.xlabel("Days from Cumulative cases = 100")
plt.ylabel("Cumulative Covid cases ")
plt.title("First Wave of USA")
plt.plot(x1,y1,label='United States of America', c='y')
x1, y1 = [1.1, 57.2], [-14.97, -6.09]
plt.plot(x1, y1, '--g')
x1, y1 = [57.2, 199.8], [-6.09, -3.94]
plt.plot(x1, y1, '--r')
plt.grid()
plt.show()
# finding slope and intercept
x1 = np.arange(1, 57)
USA_firstsegment = USA_first_wave[1:57]
y1 = USA_firstsegment
USA_slope_intercept1 = np.polyfit(x1, y1, 1)
print("USA First wave- slope & intercept")
print(USA_slope_intercept1)
slope = 0.18198125
intercept = -14.68616447
USA_exp_model1 = np.exp(intercept + slope * x1)
y1 = USA_exp_model1
y2 = normalised_USA_dataset[1:57]
y3 = y2 - y1
plt.title("Exponential growth of USA for first segment in Wave 1 ")
plt.xlabel("Days")
plt.ylabel("Number of cases")
plt.plot(x1, y1 ,label="Predicted wave",c="r")
plt.plot(x1, y2 ,label="Observed wave",c="b")
plt.plot(x1, y3, label = "Error", c="c")
plt.grid()
plt.legend()
plt.show()
# prediction of 1st USA wave
x1 = np.arange(1,232)
x2 = np.arange(1,57)
y1 = normalised_USA_dataset[1:232]
USA_exp_model_firstwave = np.exp(intercept + slope * x1)
y1 = USA_exp_model1
y2 = normalised_USA_dataset[1:232]
y3 = y2[1:57] - y1
plt.title("Exponential growth of USA for first Wave ")
plt.xlabel("Days")
plt.ylabel("Number of cases")
sns.lineplot(x2,y1)
sns.lineplot(x1, y2)
sns.lineplot(x2, y3)
plt.legend(labels=["Predicted","Observed", "Error"])
plt.grid()
plt.show()