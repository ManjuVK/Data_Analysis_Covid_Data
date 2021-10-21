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
# first wave
x1, y1 = [26.0, 104.2 ], [-17.36, -6.33]
plt.plot(x1, y1, '--g')
x1, y1 = [104.2, 258.5], [-6.33, -5.17]
plt.plot(x1, y1, '--r')
#second wave
x1, y1 = [258.6,401.7 ], [-5.17, -2.82]
plt.plot(x1, y1, '--g')
x1, y1 = [401.8, 626], [-2.82, -2.24]
plt.plot(x1, y1, '--r')
#third wave
#x1, y1 = [252.4, 321.8], [-5.23, -3.75]
#plt.plot(x1, y1, '--g')
#x1, y1 = [321.9, 360.8], [-3.75, -3.30]
#plt.plot(x1, y1, '--r')
#fourth wave
#x1, y1 = [360.9, 396.2], [-3.30, -2.77]
#plt.plot(x1, y1, '--g')
#x1, y1 = [396.3, 532.5], [-2.77, -2.66]
#plt.plot(x1, y1, '--r')
#fifth wave
#x1, y1 = [532.6, 615], [-2.66, -2.24]
#plt.plot(x1, y1, '--g')
#plt.legend()
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
#first wave
x1, y1 = [22.9, 99.2], [-17.26, -5.95]
plt.plot(x1, y1, '--g')
x1, y1 = [99.2, 273.4], [-5.95, -5.20]
plt.plot(x1, y1, '--r')
#second wave
x1, y1 = [273.5, 474.3], [-5.20, -2.68]
plt.plot(x1, y1, '--g')
x1, y1 = [474.3, 626], [-2.68, -2.55]
plt.plot(x1, y1, '--r')
#third wave
#x1, y1 = [272.9, 319.9], [-5.2, -3.79]
#plt.plot(x1, y1, '--g')
#x1, y1 = [319.9, 381.3], [-3.79, -3.17]
#plt.plot(x1, y1, '--r')
#fourth wave
#x1, y1 = [381.3, 477.4], [-3.17, -2.69]
#plt.plot(x1, y1, '--g')
#x1, y1 = [477.4, 615], [-2.69, -2.59]
#plt.plot(x1, y1, '--r')
#plt.legend()
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
#first wave
x1, y1 = [15, 102.2], [-18, -6.21]
plt.plot(x1, y1, '--g')
x1, y1 = [102.2, 216.4], [-6.21, -4.22]
plt.plot(x1, y1, '--r')
#second wave
x1, y1 = [216.4, 390.6], [-4.22, -2.48]
plt.plot(x1, y1, '--g')
x1, y1 = [390.6, 626], [-2.48, -2.07]
plt.plot(x1, y1, '--r')
#third wave
#x1, y1 = [165.6, 218.8], [-5.01, -4.10]
#plt.plot(x1, y1, '--g')
#x1, y1 = [218.9, 313.7], [-4.07, -3.47]
#plt.plot(x1, y1, '--r')
#fourth wave
#x1, y1 = [313.8, 391.2], [-3.46, -2.50]
#plt.plot(x1, y1, '--g')
#x1, y1 = [394.9, 614.4], [-2.51, -2.02]
#plt.plot(x1, y1, '--r')
#plt.legend()
plt.show()

#******************************************* SLOPE-INTERCEPT   ****************************************************

#                               ************ UNITED KINGDOM ***************
#first_wave_Uk
first_wave_UK = log_Uk_dataset[27:258]
print(log_Uk_dataset)
x1 = np.arange(1,232)
y1 = first_wave_UK
UK_slope_intercept1 = np.polyfit(x1, y1, 1)
print("         UK SLOPE INTERCEPT 1")
print(UK_slope_intercept1)
# second_wave_UK
second_wave_UK = log_Uk_dataset[259:625]
x1 = np.arange(1,367)
y1 = second_wave_UK
UK_slope_intercept2 = np.polyfit(x1, y1, 1)
print("         UK SLOPE INTERCEPT 2")
print(UK_slope_intercept2)
# third_wave_UK
#third_wave_UK = log_Uk_dataset[254:361]
#x1 = np.arange(1,108)
#y1 = third_wave_UK
#UK_slope_intercept3 = np.polyfit(x1, y1, 1)
#print("         UK SLOPE INTERCEPT 3")
#print(UK_slope_intercept3)
# fourth_wave_UK
#fourth_wave_UK = log_Uk_dataset[362:533]
#x1 = np.arange(1,172)
#y1 = fourth_wave_UK
#UK_slope_intercept4 = np.polyfit(x1, y1, 1)
#print("         UK SLOPE INTERCEPT 4")
#print(UK_slope_intercept4)
# fifth_wave_UK
#fifth_wave_UK = log_Uk_dataset[534:626]
#x1 = np.arange(1,93)
#y1 = fifth_wave_UK
#UK_slope_intercept5 = np.polyfit(x1, y1, 1)
#print("         UK SLOPE INTERCEPT 5")
#print(UK_slope_intercept5)


#                               *********** ITALY ********************
# first_wave_Italy
first_wave_Italy = log_Italy_dataset[25:273]
x1 = np.arange(1,249)
y1 = first_wave_Italy
Italy_slope_intercept1 = np.polyfit(x1, y1, 1)
print("         ITALY SLOPE INTERCEPT 1")
print(Italy_slope_intercept1)
# second_wave_Italy
second_wave_Italy = log_Italy_dataset[273:625]
x1 = np.arange(1,353)
y1 = second_wave_Italy
Italy_slope_intercept2 = np.polyfit(x1, y1, 1)
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
