#                               IMPORT LIBRARIES

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#                               READ DATASET
dataset = pd.read_csv("./WHO-COVID-19-global-data (1).csv")
Covid_cases = dataset['Cumulative_cases']
The_Untited_Kingdom = Covid_cases[132299:132926]
Italy = Covid_cases[64583:65210]
United_States_of_America = Covid_cases[141704:142331]

#*********************************************** TASK 1-3 ***********************************************************
# Plot the data
x1 = np.arange(1,628)
y1 = The_Untited_Kingdom
y2 = Italy
y3 = United_States_of_America
plt.xticks(np.arange(1,628,50))
plt.xlim(xmin=0)
plt.xticks(rotation=0)
plt.xlabel("Days from begining of epidemic")
plt.ylabel("Number of Covid cases(in millions)")
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
plt.ylabel("Number of Covid cases(in millions)")
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
plt.ylabel("Number of Covid cases(in millions)")
plt.title("Normalised Cumulative cases of United States, Italy from 24.02.2020 to 20.09.2021")
plt.plot(x1,y1,label='Italy', c='c')
plt.plot(x1,y2,label='United States of America', c='y')
plt.tight_layout()
plt.grid()
plt.legend()
plt.show()

#****************************************** TASK 5 *****************************************************************
# Taking log of normalised data
# UK
x1 = np.arange(1, 567)
log_Uk_dataset = np.log(normalised_United_Kingdom_dataset)
log_Uk_dataset = log_Uk_dataset.dropna()
y1 = log_Uk_dataset
UK_first_wave = y1[1:201]

normalised_firstwave = normalised_United_Kingdom_dataset[1:201]
normalised_secondwave = normalised_United_Kingdom_dataset[201:]
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
# normalised graph of wave 1
#normalised_firstwave = normalised_United_Kingdom_dataset[1:201]
#normalised_secondwave = normalised_United_Kingdom_dataset[201:]
#y1 = normalised_firstwave
#x1 = np.arange(1,201)
#plt.xticks(np.arange(1,201,50))
#plt.xlim(xmin=0)
#plt.xticks(rotation=0)
#plt.xlabel("Days from Cumulative cases = 100")
#plt.ylabel("Cumulative Covid cases")
#plt.title("Normalised graph of United Kingdom_Wave 1")
#plt.plot(x1,y1,label='The Untited Kingdom', c='y')
#plt.grid()
#plt.show()
# ***************************************************** UK first wave ***************************************
x1 = np.arange(1,201)
y1 = UK_first_wave
plt.xticks(np.arange(1,201,50))
plt.xlabel("Number of Days")
plt.ylabel("Cumulative cases")
plt.title("Logarithmic graph of UK_first wave")
plt.plot(x1, y1,label="UK First Wave", c="y")
x1, y1 = [0.8, 37], [-12.43, -6.67]
plt.plot(x1, y1, '--g')
x1, y1 = [37, 199], [-6.67, -5.11]
plt.plot(x1, y1, '--r')
plt.grid()
plt.show()
#                           finding slope and intercept(Exponential)
x1 = np.arange(1,38)
UK_firstsegment = UK_first_wave[1:38]
y1 = UK_firstsegment
UK_slope_intercept1 = np.polyfit(x1, y1, 1)
print("UK First wave(Exponential)- slope & intercept")
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
x2 = np.arange(1,50)
y1 = normalised_United_Kingdom_dataset[1:201]
UK_exp_model_firstwave = np.exp(intercept + slope * x1)
y1 = UK_exp_model_firstwave[1:50]
y2 = normalised_United_Kingdom_dataset[1:201]
y3 = y2[1:50] - y1
plt.title("Exponential growth of UK_First Wave ")
plt.xlabel("Days")
plt.ylabel("Number of cases")
sns.lineplot(x2,y1)
sns.lineplot(x1, y2)
sns.lineplot(x2, y3)
plt.legend(labels=["Predicted","Observed", "Error"])
plt.grid()
error = sum((normalised_United_Kingdom_dataset[1:201]-UK_exp_model_firstwave)**2)
print("Error of Exponential-wave 1")
print(error)
#plt.legend()
plt.show()
#                           finding k_value(logistic)
x1 = normalised_United_Kingdom_dataset[1:201]
k_value = x1 * (1 + UK_exp_model_firstwave)/UK_exp_model_firstwave
print("K VALUE of UK_first wave")
f = k_value.to_numpy()
print("********************F")
print(f)
print(k_value)
x1 = np.arange(1,201)
y1 = k_value

plt.title("K value for Wave 1- The United Kingdom")
plt.xlabel("Days")
plt.ylabel("Carrying Capacity")
plt.plot(x1, y1)
plt.show()
used_k_value = 0.00477107
norm_data_UKFirstwave = normalised_United_Kingdom_dataset[1:201]
est_log_model = np.log(abs(norm_data_UKFirstwave/((used_k_value)-(norm_data_UKFirstwave))))
#print(est_log_model)
# find slope of logistic
y1 = est_log_model
x2 = np.arange(1,201)
est_log_slope  = np.polyfit(x2, y1, 1)
print("Slope Intercept of Logistic(wave 1)")
print(est_log_slope)
slope = 0.03458301
intercept = -3.29141529
exponential_log = np.exp(est_log_slope[1] + est_log_slope[0] * x2)
Logistic_model = used_k_value * exponential_log/(1+exponential_log)
#print("Logistic")
#print(Logistic_model)
error = norm_data_UKFirstwave - Logistic_model
SSE_Logistic_UKWave1 = sum(error**2)
print("Error of Logistic model(wave 1)")
print(SSE_Logistic_UKWave1)
#ln(P/K-P) UKWAVE1
x1 = np.arange(1,201)
y1 = est_log_model
y2 = est_log_slope[1]+est_log_slope[0]*x1
plt.xlabel("Days")
plt.ylabel("Ln(P)/(K-P)")
plt.plot(x1, y1,label="Observed", c="g")
plt.plot(x1,y2,label="Predicted",c="r")
plt.legend()
plt.grid()
plt.show()

x1 = np.arange(1,201)
y1 = Logistic_model
y2 =norm_data_UKFirstwave
plt.title("Logistic Model Prediction for Wave 1-UK")
plt.ylabel("Cumulative fraction")
plt.xlabel("Days from begining")
plt.plot(x1,y1,label='Logistic',c='r')
plt.plot(x1,y2,label='Observed',c='g')
plt.legend()
plt.show()
#                           initial value of k
used_k_value = 0.41199605
norm_data_UKFirstwave = normalised_United_Kingdom_dataset[1:201]
est_log_model = np.log(abs(norm_data_UKFirstwave/((used_k_value)-(norm_data_UKFirstwave))))
print(est_log_model)
# find slope of logistic
y1 = est_log_model
x2 = np.arange(1,201)
est_log_slope  = np.polyfit(x2, y1, 1)
print("Slope Intercept of Logistic(wave 1)with initial value f k")
print(est_log_slope)
slope = 0.03458301
intercept = -3.29141529
exponential_log = np.exp(est_log_slope[1] + est_log_slope[0] * x2)
Logistic_model = used_k_value * exponential_log/(1+exponential_log)
#print("Logistic")
#print(Logistic_model)
error = norm_data_UKFirstwave - Logistic_model
SSE_Logistic_UKWave1 = sum(error**2)
print("Error of Logistic model(wave 1)with initial value of k")
print(SSE_Logistic_UKWave1)
x1 = np.arange(1,201)
y1 = Logistic_model
y2 =norm_data_UKFirstwave
plt.title("Logistic Model Prediction for Wave 1-UK")
plt.ylabel("Cumulative fraction")
plt.xlabel("Days from begining")
plt.plot(x1,y1,label='Logistic',c='r')
plt.plot(x1,y2,label='Observed',c='g')
plt.legend()
plt.show()
#**************************************************** UK second wave*********************************************

x1 = np.arange(1,364)
y1 = normalised_United_Kingdom_dataset[201:]
#x = normalised_United_Kingdom_dataset[200:201]
second_wave_data = (normalised_United_Kingdom_dataset[201:]-0.006021)
print(second_wave_data)
UK_second_wave = np.log(second_wave_data)
UK_second_wave = UK_second_wave.dropna()
print(UK_second_wave)
y1 = UK_second_wave
plt.xticks(np.arange(1,364,50))
plt.xlabel("Number of Days")
plt.ylabel("Cumulative cases")
plt.title("Second wave of UK")
plt.plot(x1, y1,label="UK Second Wave", c="y")
x1, y1 = [2.2,69.6 ], [-9.43, -3.97]
plt.plot(x1, y1, '--g')
x1, y1 = [69.6, 363.4], [-3.97, -2.26]
plt.plot(x1, y1, '--r')
plt.grid()
plt.show()
#normalised graph of wave 2
#x1 = np.arange(1,364)
#y1 = normalised_secondwave[:-2]
#plt.xticks(np.arange(1,364,50))
#plt.xlabel("Number of Days")
#plt.ylabel("Cumulative cases")
#plt.title("Normalised graph of United Kingdom_Wave2")
#plt.plot(x1, y1,label="UK Second Wave", c="y")
#plt.grid()
#plt.show()
#finding slope and intercept
x1 = np.arange(1,70)
UK_firstsegment2 = UK_second_wave[1:70]
y1 = UK_firstsegment2
UK_slope_intercept1 = np.polyfit(x1, y1, 1)
print("UK Second wave- slope & intercept(Exponential)")
print(UK_slope_intercept1)
slope = 0.05313022
intercept = -7.05400091
UK_exp_model1 = np.exp(intercept + slope * x1)
y1 = UK_exp_model1
y2 = second_wave_data[1:70]
y3 = y2 - y1
plt.title("Exponential growth of UK for first segment in Wave 2 ")
plt.xlabel("Days")
plt.ylabel("Number of cases")
plt.plot(x1, y1 ,label="Predicted wave",c="r")
plt.plot(x1, y2 ,label="Observed wave",c="b")
plt.plot(x1, y3, label = "Error", c="c")
plt.grid()
plt.legend()
plt.show()

#prediction for 2nd UK wave
x1 = np.arange(1,364)
x2 = np.arange(1,90)
y1 = second_wave_data[:-2]
UK_exp_model_secondwave = np.exp(intercept + slope * x1)
y1 = UK_exp_model_secondwave[1:90]
y2 = second_wave_data[:-2]
y3 = y2[1:90] - y1
plt.title("Exponential growth of UK for Second Wave ")
plt.xlabel("Days")
plt.ylabel("Number of cases")
sns.lineplot(x2,y1)
sns.lineplot(x1, y2)
sns.lineplot(x2, y3)
plt.legend(labels=["Predicted","Observed", "Error"])
plt.grid()
plt.show()
error = sum((second_wave_data[:-2]-UK_exp_model_secondwave)**2)
print("Error of Exponential-wave 2")
print(error)
#finding k_value
x1 = second_wave_data[:-2]
k_value = x1 * (1 + UK_exp_model_secondwave)/UK_exp_model_secondwave
f = k_value.to_numpy()
print("K VALUE of second wave")
print(f)
x1 = np.arange(1,364)
y1 = k_value
plt.title("K value for Wave 2- The United Kingdom")
plt.xlabel("Days")
plt.ylabel("Carrying Capacity")
plt.plot(x1, y1)
plt.show()
used_k_value = 0.103424
norm_data_UKSecondwave = second_wave_data[:-2]
est_log_model = np.log(abs(norm_data_UKSecondwave/((used_k_value)-(norm_data_UKSecondwave))))
print(est_log_model)
# find slope of logistic
y1 = est_log_model
x2 = np.arange(1,364)
est_log_slope = np.polyfit(x2, y1, 1)
print(" Slope Intercept of Logistic model (wave 2)")
print(est_log_slope)
slope = 0.01444578# .01390938 #0.03458301
intercept = -1.745269330#-1.67991815#-3.29141529
exponential_log = np.exp(est_log_slope[1] + est_log_slope[0] * x2)
Logistic_model = used_k_value * exponential_log/(1+exponential_log)
print("Logistic")
print(Logistic_model)
error = norm_data_UKSecondwave - Logistic_model
SSE_logistic_UKWave2 = sum(error**2)
print("Error")
print(SSE_logistic_UKWave2)
# plot log graphs of ln(p)/ wave1
x1 = np.arange(1,364)
y1 = est_log_model
y2 = est_log_slope[1]+est_log_slope[0]*x1
plt.xlabel("Days")
plt.ylabel("Ln(P)/(K-P)")
plt.plot(x1, y1,label="Observed", c="g")
plt.plot(x1,y2,label="Predicted",c="r")
plt.legend()
plt.grid()
plt.show()
x1 = np.arange(1,364)
y1 = Logistic_model
y2 = norm_data_UKSecondwave
plt.title("Logistic Model Prediction for Wave 2-UK")
plt.ylabel("Cumulative fraction")
plt.xlabel("Days from begining")
plt.plot(x1,y1,label='Logistic',c='r')
plt.plot(x1,y2,label='Observed',c='g')
plt.legend()
plt.show()
#                       wave2 with initial value of k
used_k_value = 0.09090431
norm_data_UKSecondwave = second_wave_data[:-2]
est_log_model = np.log(abs(norm_data_UKSecondwave/((used_k_value)-(norm_data_UKSecondwave))))
print(est_log_model)
# find slope of logistic
y1 = est_log_model
x2 = np.arange(1,364)
est_log_slope = np.polyfit(x2, y1, 1)
print(" Slope Intercept of Logistic model with initial value of k(wave 2)")
print(est_log_slope)
slope = 0.01444578# .01390938 #0.03458301
intercept = -1.745269330#-1.67991815#-3.29141529
exponential_log = np.exp(est_log_slope[1] + est_log_slope[0] * x2)
Logistic_model = used_k_value * exponential_log/(1+exponential_log)
#print("Logistic")
#print(Logistic_model)
error = norm_data_UKSecondwave - Logistic_model
SSE_logistic_UKWave2 = sum(error**2)
print("Error with initial value of k)")
print(SSE_logistic_UKWave2)
x1 = np.arange(1,364)
y1 = Logistic_model
y2 = norm_data_UKSecondwave
plt.title("Logistic Model Prediction for Wave 2-UK")
plt.ylabel("Cumulative fraction")
plt.xlabel("Days from begining")
plt.plot(x1,y1,label='Logistic',c='r')
plt.plot(x1,y2,label='Observed',c='g')
plt.legend()
plt.show()

