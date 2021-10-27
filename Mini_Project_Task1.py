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

#**************************************** TASK 6 **********************************************************************
#   Normalise Cumulative data

normalised_United_Kingdom_dataset =  The_Untited_Kingdom[0:627]/67886011
normalised_Italy_dataset = Italy[0:627]/60461826
normalised_USA_dataset = United_States_of_America[0:627]/331002651
x1 = np.arange(1,628)
y1 = normalised_United_Kingdom_dataset
y2 = normalised_Italy_dataset
y3 = normalised_USA_dataset
plt.xticks(np.arange(1,628,50))
plt.xlim(xmin=0)
plt.xticks(rotation=0)
plt.xlabel("Days from begining of epidemic")
plt.ylabel("Number of Covid cases")
plt.title("Normalised Cumulative Covid cases of United Kingdom, Italy, USA from 03.01.2020 to 20.09.2021")
plt.plot(x1,y1,label='The Untited Kingdom', c='m')
plt.plot(x1,y2,label= 'Italy', c='y')
plt.plot(x1,y3,label= 'United States of America', c='c')
plt.legend()
plt.grid()
plt.show()
#***************************************  TASK 7 **********************************************************************
#       THE UNITED KINGDOM
x1 = np.arange(1,566)
log_Uk_dataset = np.log(normalised_United_Kingdom_dataset)
log_Uk_dataset = log_Uk_dataset.dropna()
y1 = log_Uk_dataset[61:626]
UK_first_wave = y1[1:200]
UK_second_wave = y1[200:566]
plt.xticks(np.arange(1,566,50))
plt.xlim(xmin=0)
plt.xticks(rotation=0)
plt.xlabel("Days from Cumulative cases = 100")
plt.ylabel("Cumulative Covid cases")
plt.title("Logarithmic graph for United Kingdom from 04.03.2020 to 20.09.2021")
plt.plot(x1,y1,label='The Untited Kingdom', c='y')
# first wave
x1, y1 = [1.1, 42], [-12.65, -6.03]
plt.plot(x1, y1, '--g')
x1, y1 = [55.5, 201.6], [-6.03, -5.07]
plt.plot(x1, y1, '--r')
#second wave
x1, y1 = [201.6,340.5 ], [-5.07, -2.81]
plt.plot(x1, y1, '--g')
x1, y1 = [340.5, 550.4], [-2.81, -2.32]
plt.plot(x1, y1, '--r')
plt.grid()
plt.show()
#****************************** SLOPE INTERCEPT*******************************88
# first_wave_Uk
x1 = np.arange(1,200)
y1 = UK_first_wave
plt.xticks(np.arange(1,200,50))
plt.xlim(xmin=0)
plt.xticks(rotation=0)
plt.xlabel("Days from begining of epidemic")
plt.ylabel("Cumulative Covid cases")
plt.title("Expected model prediction for Wave 1- The United Kingdom")
plt.plot(x1,y1,label='The Untited Kingdom', c='b')
# first wave
x1, y1 = [0.9, 55.5], [-12.39, -6.03]
plt.plot(x1, y1, '--g')
x1, y1 = [55.5, 201.6], [-6.03, -5.07]
plt.plot(x1, y1, '--r')
plt.grid()
plt.show()
#first segment
x1 = np.arange(1,38)
y1 = UK_first_wave[1:38]
UK_slope_intercept1 = np.polyfit(x1, y1, 1)
print("         UK SLOPE INTERCEPT 1")
print(UK_slope_intercept1)
slope = 0.15483199
intercept = -11.70299942
UK_exp_model1 = np.exp(intercept + slope * x1)
print("UK_EXPECTED MODEL")
print(UK_exp_model1)
y1 = normalised_United_Kingdom_dataset[61:98]
y2 = UK_exp_model1
y3 = y1 - y2
plt.xticks(np.arange(1,38,5))
plt.title("Expected model prediction for Wave 1- The United Kingdom")
plt.plot(x1,y1,label='Observed wave', c='b')
plt.plot(x1,y2,label= 'Predicted wave', c='r')
plt.plot(x1,y3,label= 'Error', c='c')
plt.legend()
plt.show()


#
x1 = np.arange(1,200)
y1 = UK_first_wave
#UK_slope_intercept1 = np.polyfit(x1, y1, 1)
#print("         UK SLOPE INTERCEPT 1")
#print(UK_slope_intercept1)
slope = 0.15483199
intercept = -11.70299942
UK_exp_model1 = np.exp(intercept + slope * x1)
print("UK_EXPECTED MODEL")
print(UK_exp_model1)
y1 = normalised_United_Kingdom_dataset[61:260]
y2 = UK_exp_model1
y3 = y1 - y2
plt.xticks(np.arange(1,200,50))
plt.title("Expected model prediction for Wave 1- The United Kingdom")
plt.plot(x1,y1,label='Observed wave', c='b')
plt.plot(x1,y2,label= 'Predicted wave', c='r')
plt.plot(x1,y3,label= 'Error', c='c')
plt.legend()
plt.show()

#second wave
x1 = np.arange(1,366)
y1 = UK_second_wave
plt.xticks(np.arange(1,366,50))
plt.xlim(xmin=0)
plt.xticks(rotation=0)
plt.xlabel("Days from begining of epidemic")
plt.ylabel("Cumulative Covid cases")
plt.title("Expected model prediction for Wave 2- The United Kingdom")
plt.plot(x1,y1,label='The Untited Kingdom', c='b')
x1, y1 = [1.4,127 ], [-5.095, -2.890]
plt.plot(x1, y1, '--g')
x1, y1 = [127, 350.3], [-2.890, -2.252]
plt.plot(x1, y1, '--r')
plt.grid()
plt.show()
#first segment
x1 = np.arange(1,126)
y1 = UK_second_wave[1:126]
UK_slope_intercept2 = np.polyfit(x1, y1, 1)
print("         UK SLOPE INTERCEPT WAVE 2")
print(UK_slope_intercept2)
slope = .01719461
intercept = -4.96773991
UK_exp_model2 = np.exp(intercept + slope * x1)
print("UK_EXPECTED MODEL")
print(UK_exp_model1)
y1 = normalised_United_Kingdom_dataset[262:387]
y2 = UK_exp_model2
y3 = y1 - y2
plt.xticks(np.arange(1,200,50))
plt.title("Expected model prediction for Wave 2- The United Kingdom")
plt.plot(x1,y1,label='Observed wave', c='b')
plt.plot(x1,y2,label= 'Predicted wave', c='r')
plt.plot(x1,y3,label= 'Error', c='c')
plt.legend()
plt.show()
# FIND K_VALUE of 1st wave
x1 = normalised_United_Kingdom_dataset[61:260]
y1 = x1*(1 + UK_exp_model1)/UK_exp_model1
plt.title("K value for Wave 1- The United Kingdom")
plt.plot(x1, y1)
plt.show()
print("K VALUE")
print(y1)
used_k_value =0.005871
log_absvalue = np.log(abs(x1/(used_k_value-x1)))
y1 = log_absvalue
x2 = np.arange(1,200)
print("ABS VALUE")
print(log_absvalue)
#slope of abs value
log_abs_value_slope = np.polyfit(x2, y1, 1)
print("slope intercept of abs value")
print(log_abs_value_slope)
slope = 0.03394197
intercept = -3.3821157
exp_log_abs = np.exp(intercept+slope*x2)
Logistic_model = used_k_value * exp_log_abs/(1+exp_log_abs)
print("Logistic")
print(Logistic_model)
error = x1 - Logistic_model
x1 = np.arange(1,200)
y1 = Logistic_model
y2 = normalised_United_Kingdom_dataset[61:260]
plt.plot(x1,y1,label='Logistic',c='r')
plt.plot(x1,y2,label='Observed',c='g')
plt.show()


#       ITALY
x1 = np.arange(1,575)
log_Italy_dataset = np.log(normalised_Italy_dataset)
log_Italy_dataset = log_Italy_dataset.dropna()
y1 = log_Italy_dataset[52:626]
Italy_first_wave = y1[1:230]
Italy_second_wave = y1[231:575]
print(y1.count())
plt.xticks(np.arange(1,575,50))
plt.xlim(xmin=0)
plt.xticks(rotation=0)
plt.xlabel("Days from Cumulative cases = 100")
plt.ylabel("Cumulative  Covid cases ")
plt.title("Logarithmic graph for Italy from 24.02.2020 to 20.09.2021")
plt.plot(x1,y1,label='Italy', c='y')
#first wave
x1, y1 = [1.7, 48.3], [-12.11, -6.02]
plt.plot(x1, y1, '--g')
x1, y1 = [48.3, 231.6], [-6.02, -5.11]
plt.plot(x1, y1, '--r')
#second wave
x1, y1 = [231.6, 282.2], [-5.11, -3.62]
plt.plot(x1, y1, '--g')
x1, y1 = [282.2, 550], [-3.62, -2.60]
plt.plot(x1, y1, '--r')
plt.grid()
plt.show()

#   UNITED STATES OF AMERICA
x1 = np.arange(1,575)
log_USA_dataset = np.log(normalised_USA_dataset)
log_USA_dataset = log_USA_dataset.dropna()
y1 = log_USA_dataset[52:626]
USA_first_wave = y1[1:232]
USA_second_wave = y1[233:575]
print(y1)
plt.xticks(np.arange(1,575,50))
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

#******************************************* TASK 8 *******************************************************************
#                                           SLOPE-INTERCEPT

#                               ************ UNITED KINGDOM ***************

#plt.xticks(np.arange(1,200,25))
#plt.title("Expected model prediction for Wave 1- The United Kingdom")
#plt.plot(x1,y1,label='Observed wave', c='b')
#plt.plot(x1,y2,label= 'Predicted wave', c='r')
#plt.plot(x1,y3,label= 'Error', c='c')
#plt.legend()
#plt.show()






# first_segment

#x1 = np.arange(1,210)
#y1 = log_Uk_dataset[51:112]
#

y1 = log_Uk_dataset[51:260]
slope = 0.15778639
intercept = -14.2349729



# second_wave_UK
x1 = np.arange(1,300)
y1 = UK_second_wave
print(UK_second_wave.count())
print(UK_first_wave.count())
print(UK_third_wave.count())
UK_slope_intercept2 = np.polyfit(x1, y1, 1)
print("         UK SLOPE INTERCEPT 2")
print(UK_slope_intercept2)
# third_wave_UK
x1 = np.arange(1,74)
y1 = UK_third_wave
UK_slope_intercept3 = np.polyfit(x1, y1, 1)
print("         UK SLOPE INTERCEPT 3")
print(UK_slope_intercept3)
#


#                               *********** ITALY ********************
# first_wave_Italy
first_wave_Italy = log_Italy_dataset[25:273]
x1 = np.arange(1,201)
y1 = first_wave_Italy
Italy_slope_intercept1 = np.polyfit(x1, y1, 1)
slope = 0.334
intercept = -11.35
Italy_exp_model = (intercept + slope *first_wave_Italy)
print(Italy_exp_model)
y2 = Italy_exp_model
plt.plot(x1,y1,label='Observed wave', c='b')
plt.plot(x1,y2,label= 'predicted wave', c='r')
plt.legend()
plt.show()
print(Italy_slope_intercept1)
# second_wave_Italy
second_wave_Italy = log_Italy_dataset[273:626]
x1 = np.arange(1,354)
y1 = second_wave_Italy
Italy_slope_intercept2 = np.polyfit(x1, y1, 1)
slope = 0.0057
intercept = -4.16
Italy_exp_model2 = (intercept + slope *second_wave_Italy)
print(Italy_exp_model2)
y2 = Italy_exp_model2
plt.plot(x1,y1,label='Observed wave', c='b')
plt.plot(x1,y2,label= 'predicted wave', c='r')
plt.legend()
plt.show()

print("         ITALY SLOPE INTERCEPT 2")
print(Italy_slope_intercept2)


#                               ************ USA **********************
# first_wave_USA
first_wave_USA = log_USA_dataset[26:216]
x1 = np.arange(1,191)
y1 = first_wave_USA
USA_slope_intercept1 = np.polyfit(x1, y1, 1)
print("         USA SLOPE INTERCEPT 1")
print(USA_slope_intercept1)
# second_wave_USA
second_wave_USA = log_USA_dataset[216:625]
x1 = np.arange(1,410)
y1 = second_wave_USA
USA_slope_intercept2 = np.polyfit(x1, y1, 1)
print("         USA SLOPE INTERCEPT 2")
print(USA_slope_intercept2)
