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
#normalised data of first wave
#x1 = np.arange(1,232)
#y1 = normalised_USA_dataset[1:232]
#USA_first_wave = y1[1:232]
#USA_second_wave = y1[233:576]
#plt.xticks(np.arange(1,233,50))
#plt.xlim(xmin=0)
#plt.xticks(rotation=0)
#plt.xlabel("Days from Cumulative cases = 100")
#plt.ylabel("Cumulative Covid cases ")
#plt.title("Normalised graph for United States of America_Wave 1")
#plt.plot(x1,y1,label='United States of America', c='y')
#plt.grid()
#plt.show()
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
print("USA First wave- slope & intercept Exponential")
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
x2 = np.arange(1,70)
y1 = normalised_USA_dataset[1:232]
USA_exp_model_firstwave = np.exp(intercept + slope * x1)
y1 = USA_exp_model_firstwave[1:70]
y2 = normalised_USA_dataset[1:232]
y3 = y2[1:70] - y1
plt.title("Exponential growth of USA for first Wave ")
plt.xlabel("Days")
plt.ylabel("Number of cases")
sns.lineplot(x2,y1)
sns.lineplot(x1, y2)
sns.lineplot(x2, y3)
plt.legend(labels=["Predicted","Observed", "Error"])
plt.grid()
plt.show()
exp_error = sum((normalised_USA_dataset[1:230]-USA_exp_model_firstwave[1:230])**2)
print("Error of Exponential growth")
print(exp_error)
# finding k value
x1 = normalised_USA_dataset[1:232]
k_value = x1 * (1 + USA_exp_model_firstwave)/USA_exp_model_firstwave
print("k value of USA first wave")
f = k_value.to_numpy()
print("************************f")
print(f)
print(k_value)
x1 = np.arange(1,232)
y1 = k_value
plt.title("K value for Wave 1- United States of America")
plt.xlabel("Days")
plt.ylabel("Carrying Capacity")
plt.plot(x1, y1)
plt.show()
used_k_value = 0.02023205
norm_data_USAFirstwave = normalised_USA_dataset[1:232]
est_log_model = np.log(abs(norm_data_USAFirstwave/((used_k_value)-(norm_data_USAFirstwave))))
print(est_log_model)
# find slope of logistic
y1 = est_log_model
x2 = np.arange(1,232)
est_log_slope  = np.polyfit(x2, y1, 1)
print("Slope Intercept of first wave(Logistic)")
print(est_log_slope)
slope = 0.04559845
intercept = - 6.55652335
exponential_log = np.exp(est_log_slope[1] + est_log_slope[0] * x2)
Logistic_model = used_k_value * exponential_log/(1+exponential_log)
print("Logistic")
print(Logistic_model)
error = norm_data_USAFirstwave - Logistic_model
SSE_Logistic_USAWave1 = sum(error**2)
print("Error of first wave")
print(SSE_Logistic_USAWave1)
x1 = np.arange(1,232)
y1 = Logistic_model
y2 =norm_data_USAFirstwave
plt.title("Logistic Model Prediction for Wave 1-USA")
plt.ylabel("Cumulative fraction")
plt.xlabel("Days from begining")
plt.plot(x1,y1,label='Logistic',c='r')
plt.plot(x1,y2,label='Observed',c='g')
plt.legend()
plt.show()
#                           logistic prediction with initial value of k
used_k_value = 0.66769552
norm_data_USAFirstwave = normalised_USA_dataset[1:232]
est_log_model = np.log(abs(norm_data_USAFirstwave/((used_k_value)-(norm_data_USAFirstwave))))
print(est_log_model)
# find slope of logistic
y1 = est_log_model
x2 = np.arange(1,232)
est_log_slope  = np.polyfit(x2, y1, 1)
print("Slope Intercept of first wave(Logistic)with initial value of k")
print(est_log_slope)
slope = 0.04559845
intercept = - 6.55652335
exponential_log = np.exp(est_log_slope[1] + est_log_slope[0] * x2)
Logistic_model = used_k_value * exponential_log/(1+exponential_log)
#print("Logistic")
#print(Logistic_model)
error = norm_data_USAFirstwave - Logistic_model
SSE_Logistic_USAWave1 = sum(error**2)
print("Error of first wave(with initial value of k")
print(SSE_Logistic_USAWave1)
x1 = np.arange(1,232)
y1 = Logistic_model
y2 =norm_data_USAFirstwave
plt.title("Logistic Model Prediction for Wave 1-USA")
plt.ylabel("Cumulative fraction")
plt.xlabel("Days from begining")
plt.plot(x1,y1,label='Logistic',c='r')
plt.plot(x1,y2,label='Observed',c='g')
plt.legend()
plt.show()

#********************************************** USA SECOND WAVE ************************************************
x = 0.023487
second_wave_data = (normalised_USA_dataset[232:]-0.023487)
print(second_wave_data)
USA_second_wave = np.log(second_wave_data)
USA_second_wave = USA_second_wave.dropna()
y1 = USA_second_wave
x1 = np.arange(1, 342)
plt.xticks(np.arange(1,342,50))
plt.xlabel("Number of Days")
plt.ylabel("Cumulative cases")
plt.title("Second wave of USA")
plt.plot(x1, y1,label="USA Second Wave", c="y")
x1, y1 = [0.9, 50.3], [-8.80, -3.95]
plt.plot(x1, y1, '--g')
x1, y1 = [50.3, 340.9], [-3.95, -2.28]
plt.plot(x1, y1, '--r')
plt.grid()
plt.show()
# normalised graph of USA WAVE2
#y1 = normalised_USA_dataset[232:-2]
#x1 = np.arange(1, 342)
#plt.xticks(np.arange(1,342,50))
#plt.xlabel("Number of Days")
#plt.ylabel("Cumulative cases")
#plt.title("Normalised graph of USA_Wave 2")
#plt.plot(x1, y1,label="USA Second Wave", c="y")
#plt.grid()
#plt.show()
#finding slope and intercept
x1 = np.arange(1,51)
USA_firstsegment2 = USA_second_wave[1:51]
y1 = USA_firstsegment2
USA_slope_intercept1 = np.polyfit(x1, y1, 1)
print("USA Second wave- slope & intercept(Exponential)")
print(USA_slope_intercept1)
slope = 0.0684613
intercept = -6.99039617
USA_exp_model1 = np.exp(intercept + slope * x1)
y1 = USA_exp_model1
y2 = second_wave_data[1:51]
y3 = y2 - y1
plt.title("Exponential growth of USA for first segment in Wave 2 ")
plt.xlabel("Days")
plt.ylabel("Number of cases")
plt.plot(x1, y1 ,label="Predicted wave",c="r")
plt.plot(x1, y2 ,label="Observed wave",c="b")
plt.plot(x1, y3, label = "Error", c="c")
plt.grid()
plt.legend()
plt.show()
#prediction for 2nd USA wave
x1 = np.arange(1,342)
x2 = np.arange(1,70)
y1 = second_wave_data[:-2]
USA_exp_model_secondwave = np.exp(intercept + slope * x1)
y1 = USA_exp_model_secondwave[1:70]
y2 = second_wave_data[:-2]
y3 = y2[1:70] - y1
plt.title("Exponential growth of USA for Second Wave ")
plt.xlabel("Days")
plt.ylabel("Number of cases")
sns.lineplot(x2,y1)
sns.lineplot(x1, y2)
sns.lineplot(x2, y3)
plt.legend(labels=["Predicted","Observed", "Error"])
plt.grid()
plt.show()
error = sum((second_wave_data[:-2]-USA_exp_model_secondwave)**2)
print("Error of Exponential wave 2")
print(error)
#finding k_value
x1 = second_wave_data[:-2]
k_value = x1 * (1 + USA_exp_model_secondwave)/USA_exp_model_secondwave
print("K VALUE")
f = k_value.to_numpy()
print("************************f")
print(f)
print(k_value)
x1 = np.arange(1,342)
y1 = k_value
plt.title("K value for Wave 2- United States of America")
plt.xlabel("Days")
plt.ylabel("Carrying Capacity")
plt.plot(x1, y1)
plt.show()
used_k_value = 0.10254377#.07663918#0.07638732 #0.08049084#0.08557368 #0.075
norm_data_USASecondwave = second_wave_data[:-2]
est_log_model = np.log(abs(norm_data_USASecondwave/((used_k_value)-(norm_data_USASecondwave))))
print(est_log_model)
# find slope of logistic
y1 = est_log_model
x2 = np.arange(1,342)
est_log_slope = np.polyfit(x2, y1, 1)
print("         Slope Intercept(Logistic wave 2")
print(est_log_slope)
slope = 0.01062648
intercept = -0.60874079
exponential_log = np.exp(est_log_slope[1] + est_log_slope[0] * x2)
Logistic_model = used_k_value * exponential_log/(1+exponential_log)
#print("Logistic")
#print(Logistic_model)
error = norm_data_USASecondwave - Logistic_model
SSE_logistic_USAWave2 = sum(error**2)
print("Error of Logistic_Wave 2")
print(SSE_logistic_USAWave2)
x1 = np.arange(1,342)
y1 = Logistic_model
y2 = norm_data_USASecondwave
plt.title("Logistic Model Prediction for Wave 2-USA")
plt.ylabel("Cumulative fraction")
plt.xlabel("Days from begining")
plt.plot(x1,y1,label='Logistic',c='r')
plt.plot(x1,y2,label='Observed',c='g')
plt.legend()
plt.show()
#               logistic with initial value of k
used_k_value = 0.15388505
norm_data_USASecondwave = second_wave_data[:-2]
est_log_model = np.log(abs(norm_data_USASecondwave/((used_k_value)-(norm_data_USASecondwave))))
print(est_log_model)
# find slope of logistic
y1 = est_log_model
x2 = np.arange(1,342)
est_log_slope = np.polyfit(x2, y1, 1)
print("         Slope Intercept(Logistic wave 2 with initial value of k")
print(est_log_slope)
slope = 0.01062648
intercept = -0.60874079
exponential_log = np.exp(est_log_slope[1] + est_log_slope[0] * x2)
Logistic_model = used_k_value * exponential_log/(1+exponential_log)
#print("Logistic")
#print(Logistic_model)
error = norm_data_USASecondwave - Logistic_model
SSE_logistic_USAWave2 = sum(error**2)
print("Error of Logistic_Wave 2 with initial value of k")
print(SSE_logistic_USAWave2)
x1 = np.arange(1,342)
y1 = Logistic_model
y2 = norm_data_USASecondwave
plt.title("Logistic Model Prediction for Wave 2-USA")
plt.ylabel("Cumulative fraction")
plt.xlabel("Days from begining")
plt.plot(x1,y1,label='Logistic',c='r')
plt.plot(x1,y2,label='Observed',c='g')
plt.legend()
plt.show()