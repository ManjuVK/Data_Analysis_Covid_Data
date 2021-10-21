#                               IMPORT LIBRARIES
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#                               READ DATASET
dataset = pd.read_csv("./WHO-COVID-19-global-data (1).csv")
Covid_cases = dataset['Cumulative_cases']
#date = dataset['Date_reported']
The_Untited_Kingdom = Covid_cases[132299:132925]
The_Untited_Kingdom = The_Untited_Kingdom.dropna()
Italy = Covid_cases[64583:65209]
Italy = Italy.dropna()
United_States_of_America = Covid_cases[141704:142330]
United_States_of_America = United_States_of_America.dropna()

#*********************************************** TASK 1-3 ************************************************************
# Plot the data
#Date = date[0:626]
#print(Date)
x1 = np.arange(0,626)
y1 = The_Untited_Kingdom
y2 = Italy
y3 = United_States_of_America
plt.xticks(np.arange(0,626,15))
plt.xlim(xmin=0)
plt.xticks(rotation=90)
plt.xlabel("Days from begining of epidemic")
plt.ylabel("Number of Covid cases")
plt.title("Cumulative Covid cases of United Kingdom, Italy, USA from 03.01.2020 to 20.09.2021")
plt.plot(x1,y1,label='The Untited Kingdom', c='m')
plt.plot(x1,y2,label= 'Italy', c='y')
plt.plot(x1,y3,label= 'United States of America', c='c')
plt.legend()
plt.show()

#**************************************** TASK 6 *******************************************************
#   Normalise Cumulative data

normalised_United_Kingdom_dataset =  The_Untited_Kingdom[0:626]/67886011
print("******************************** Normalised_United_Kingdom**************")
normalised_Italy_dataset = Italy[0:626]/60461826
normalised_USA_dataset = United_States_of_America[0:626]/331002651
x1 = np.arange(0,626)
y1 = normalised_United_Kingdom_dataset
y2 = normalised_Italy_dataset
y3 = normalised_USA_dataset
plt.xticks(np.arange(0,626,15))
plt.xlim(xmin=0)
plt.xticks(rotation=90)
plt.xlabel("Days from begining of epidemic")
plt.ylabel("Number of Covid cases")
plt.title("Normalised Cumulative Covid cases of United Kingdom, Italy, USA from 03.01.2020 to 20.09.2021")
plt.plot(x1,y1,label='The Untited Kingdom', c='m')
plt.plot(x1,y2,label= 'Italy', c='y')
plt.plot(x1,y3,label= 'United States of America', c='c')
plt.legend()
plt.show()
#***************************************  TASK 7 *********************************************************
#       THE UNITED KINGDOM
x1 = np.arange(0,626)
y1 = np.log(normalised_United_Kingdom_dataset)
log_Uk_dataset = np.log(normalised_United_Kingdom_dataset)
plt.xticks(np.arange(0,626,15))
plt.xlim(xmin=0)
plt.xticks(rotation=90)
plt.xlabel("Days from begining of epidemic")
plt.ylabel("Number of Covid cases")
plt.title("Normalised Cumulative Covid cases of United Kingdom from 03.01.2020 to 20.09.2021")
plt.plot(x1,y1,label='The Untited Kingdom', c='m')
x1, y1 = [26.0, 37.2 ], [-17.36, -15.95]
plt.plot(x1, y1, '--g')
x1, y1 = [37.3, 49.0], [-15.94, -15.74]
plt.plot(x1, y1, '--r')
x1, y1 = [49.1,96.1 ], [-15.74, -6.68]
plt.plot(x1, y1, '--g')
x1, y1 = [96.1, 252.3], [-6.68, -5.23]
plt.plot(x1, y1, '--r')
x1, y1 = [252.4, 321.8], [-5.23, -3.75]
plt.plot(x1, y1, '--g')
x1, y1 = [321.9, 360.8], [-3.75, -3.30]
plt.plot(x1, y1, '--r')
x1, y1 = [360.9, 396.2], [-3.30, -2.77]
plt.plot(x1, y1, '--g')
x1, y1 = [396.3, 532.5], [-2.77, -2.66]
plt.plot(x1, y1, '--r')
x1, y1 = [532.6, 615], [-2.66, -2.24]
plt.plot(x1, y1, '--g')
plt.legend()
plt.show()

#       ITALY
x1 = np.arange(0,626)
y1 = np.log(normalised_Italy_dataset)
log_Italy_dataset = np.log(normalised_Italy_dataset)
plt.xticks(np.arange(0,626,15))
plt.xlim(xmin=0)
plt.xticks(rotation=90)
plt.xlabel("Days from begining of epidemic")
plt.ylabel("Number of Covid cases ")
plt.title("Normalised Cumulative Covid cases of Italy from 03.01.2020 to 20.09.2021")
plt.plot(x1,y1,label='The Untited Kingdom', c='y')
x1, y1 = [22.9, 26], [-17.26, -16.78]
plt.plot(x1, y1, '--g')
x1, y1 = [26, 45.3], [-16.78, -16.78]
plt.plot(x1, y1, '--r')
x1, y1 = [45.3, 84.3], [-16.77, -6.43]
plt.plot(x1, y1, '--g')
x1, y1 = [84.3, 272.8], [-6.43, -5.2]
plt.plot(x1, y1, '--r')
x1, y1 = [272.9, 319.9], [-5.2, -3.79]
plt.plot(x1, y1, '--g')
x1, y1 = [319.9, 381.3], [-3.79, -3.17]
plt.plot(x1, y1, '--r')
x1, y1 = [381.3, 477.4], [-3.17, -2.69]
plt.plot(x1, y1, '--g')
x1, y1 = [477.4, 615], [-2.69, -2.59]
plt.plot(x1, y1, '--r')
plt.legend()
plt.show()

#   UNITED STATES OF AMERICA
x1 = np.arange(0,626)
y1 = np.log(normalised_USA_dataset)
log_USA_dataset = np.log(normalised_United_Kingdom_dataset)
print("******************USA")
print(y1)
plt.xticks(np.arange(0,626,15))
plt.xlim(xmin=0)
plt.xticks(rotation=90)
plt.xlabel("Days from begining of epidemic")
plt.ylabel("Number of Covid cases ")
plt.title("Normalised Cumulative Covid cases of United States of America from 03.01.2020 to 20.09.2021")
plt.plot(x1,y1,label='United States of America', c='c')
x1, y1 = [15, 22], [-18, -16]
plt.plot(x1, y1, '--g')
x1, y1 = [23, 53.9], [-16, -14.84]
plt.plot(x1, y1, '--r')
x1, y1 = [54.6, 102.2], [-14.73, -6.21]
plt.plot(x1, y1, '--g')
x1, y1 = [102.9, 165.5], [-6.20, -5.02]
plt.plot(x1, y1, '--r')
x1, y1 = [165.6, 218.8], [-5.01, -4.10]
plt.plot(x1, y1, '--g')
x1, y1 = [218.9, 313.7], [-4.07, -3.47]
plt.plot(x1, y1, '--r')
x1, y1 = [313.8, 391.2], [-3.46, -2.50]
plt.plot(x1, y1, '--g')
x1, y1 = [394.9, 614.4], [-2.51, -2.02]
plt.plot(x1, y1, '--r')
plt.legend()
plt.show()

#******************************************* SLOPE-INTERCEPT   ****************************************************

#                               ************ UNITED KINGDOM ***************
#
first_wave_UK = log_Uk_dataset[26:49]
second_wave_UK = log_Uk_dataset[50:267]
third_wave_UK = log_Uk_dataset[268:614]

#                               *********** ITALY ********************
#
first_wave_Italy = log_Italy_dataset[22:45]
second_wave_Italy = log_Italy_dataset[46:286]
third_wave_Italy = log_Italy_dataset[287:614]

#                               ************ USA **********************
#
first_wave_USA = log_USA_dataset[15:55]
second_wave_USA = log_USA_dataset[56:]