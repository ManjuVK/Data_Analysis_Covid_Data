#                               IMPORT LIBRARIES
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#                               READ DATASET
dataset = pd.read_csv("./WHO-COVID-19-global-data (1).csv")
Covid_cases = dataset['Cumulative_cases']
The_Untited_Kingdom = Covid_cases[132299:132926]
print(The_Untited_Kingdom.count())
#The_Untited_Kingdom = The_Untited_Kingdom.dropna()
Italy = Covid_cases[64583:65210]
print(Italy.count())
#Italy = Italy.dropna()
United_States_of_America = Covid_cases[141704:142331]
#United_States_of_America = United_States_of_America.dropna()
print(United_States_of_America.count())

#*********************************************** TASK 1-3 ************************************************************
# Plot the data
x1 = np.arange(1,628)
y1 = The_Untited_Kingdom
y2 = Italy
y3 = United_States_of_America
plt.xticks(np.arange(1,628,50))
plt.xlim(xmin=0)
plt.xticks(rotation=90)
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
plt.xticks(rotation=90)
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
x1 = np.arange(1,577)
log_Uk_dataset = np.log(normalised_United_Kingdom_dataset)
log_Uk_dataset = log_Uk_dataset.dropna()
y1 = log_Uk_dataset[50:626]
UK_first_wave = y1[1:201]
UK_second_wave = y1[202:501]
UK_third_wave = y1[502:577]
plt.xticks(np.arange(1,577,50))
plt.xlim(xmin=0)
plt.xticks(rotation=90)
plt.xlabel("Days from begining of epidemic")
plt.ylabel("Cumulative Covid cases")
plt.title("Logarithmic graph for United Kingdom from 03.01.2020 to 20.09.2021")
plt.plot(x1,y1,label='The Untited Kingdom', c='m')
# first wave
x1, y1 = [0, 62.2], [-15.78, -6.11]
plt.plot(x1, y1, '--g')
x1, y1 = [62.2, 201.1], [-6.11, -5.17]
plt.plot(x1, y1, '--r')
#second wave
x1, y1 = [201.1,328.3 ], [-5.17, -2.95]
plt.plot(x1, y1, '--g')
x1, y1 = [328.3, 501], [-2.95, -2.60]
plt.plot(x1, y1, '--r')
#third wave
x1, y1 = [501,551 ], [-2.60, -2.29]
plt.plot(x1, y1, '--g')
plt.grid()
plt.show()

#       ITALY
x1 = np.arange(1,577)
log_Italy_dataset = np.log(normalised_Italy_dataset)
log_Italy_dataset = log_Italy_dataset.dropna()
y1 = log_Italy_dataset[50:626]
Italy_first_wave = y1[1:231]
Italy_second_wave =y1[232:350]
Italy_third_wave = y1[351:577]
plt.xticks(np.arange(1,577,50))
plt.xlim(xmin=0)
plt.xticks(rotation=90)
plt.xlabel("Days from begining of epidemic")
plt.ylabel("Cumulative  Covid cases ")
plt.title("Logarithmic graph for Italy from 03.01.2020 to 20.09.2021")
plt.plot(x1,y1,label='Italy', c='y')
#first wave
x1, y1 = [0.6, 50.5], [-13.02, -5.94]
plt.plot(x1, y1, '--g')
x1, y1 = [50.5, 231.6], [-5.94, -5.11]
plt.plot(x1, y1, '--r')
#second wave
x1, y1 = [231.6, 277.7], [-5.11, -3.72]
plt.plot(x1, y1, '--g')
x1, y1 = [277.7, 351], [-3.72, -3.09]
plt.plot(x1, y1, '--r')
#third wave
x1, y1 = [351, 451], [-3.09, -2.65]
plt.plot(x1, y1, '--g')
x1, y1 = [451, 551], [-2.65, -2.58]
plt.plot(x1, y1, '--r')
plt.grid()
plt.show()

#   UNITED STATES OF AMERICA
x1 = np.arange(1,577)
log_USA_dataset = np.log(normalised_USA_dataset)
log_USA_dataset = log_USA_dataset.dropna()
y1 = log_USA_dataset[50:626]
USA_first_wave = y1[1:122]
USA_second_wave = y1[123:247]
USA_third_wave = y1[248:577]
print("******************USA")
print(y1)
plt.xticks(np.arange(1,577,50))
plt.xlim(xmin=0)
plt.xticks(rotation=90)
plt.xlabel("Days from begining of epidemic")
plt.ylabel("Cumulative Covid cases ")
plt.title("Logarithmic graph for United States of America from 03.01.2020 to 20.09.2021")
plt.plot(x1,y1,label='United States of America', c='c')
#first wave
x1, y1 = [1.1, 59.4], [-14.97, -6.03]
plt.plot(x1, y1, '--g')
x1, y1 = [59.4, 122.8], [-6.03, -5.01]
plt.plot(x1, y1, '--r')
#second wave
x1, y1 = [122.8, 168.9], [-5.01, -4.18]
plt.plot(x1, y1, '--g')
x1, y1 = [168.9, 248.3], [-4.18, -3.63]
plt.plot(x1, y1, '--r')
# third wave
x1, y1 = [248.3, 351], [-3.63, -2.47]
plt.plot(x1, y1, '--g')
x1, y1 = [351, 550], [-2.47, -2.12]
plt.plot(x1, y1, '--r')
plt.grid()
plt.show()

#******************************************* TASK 8 *******************************************************************
#                                           SLOPE-INTERCEPT

#                               ************ UNITED KINGDOM ***************
# first_wave_Uk
x1 = np.arange(1,201)
y1 = UK_first_wave
UK_slope_intercept1 = np.polyfit(x1, y1, 1)
print("         UK SLOPE INTERCEPT 1")
print(UK_slope_intercept1)
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
x1 = np.arange(1,76)
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
