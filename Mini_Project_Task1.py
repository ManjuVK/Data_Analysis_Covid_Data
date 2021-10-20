# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read dataset
#dataset = pd.read_csv("C:/Users/manju/OneDrive/Data Analysis For Business Intelligence/Modules/Semester_2/MA7080 Mathematical Modelling/Task 1 for miniproject/WHO-COVID-19-global-data (1).csv")
dataset = pd.read_csv("./WHO-COVID-19-global-data (1).csv")
Covid_cases = dataset['Cumulative_cases']
date = dataset['Date_reported']
The_Untited_Kingdom = Covid_cases[132299:132925]
The_Untited_Kingdom = The_Untited_Kingdom.dropna()
Italy = Covid_cases[64583:65209]
Italy = Italy.dropna()
United_States_of_America = Covid_cases[141704:142330]
United_States_of_America = United_States_of_America.dropna()

#***********************************TASK 1-3****************************************************************
# Plot the data
Date = date[0:626]
print(Date)
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

#**********************************         TASK 6    ***************************************************
#                       Normalise Cumulative data

normalised_United_Kingdom_dataset =  The_Untited_Kingdom[0:626]/67886011
print("******************************** Normalised_United_Kingdom**************")
normalised_Italy_dataset = Italy[0:626]/60461826
normalised_USA_dataset = United_States_of_America[0:626]/331002651
x1 = np.arange(0,626)
y1 = normalised_United_Kingdom_dataset
y2 = normalised_Italy_dataset
y3 = normalised_USA_dataset
#print("******************************** Normalised USA dataset")
#print(y3)
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
#******************************* TASK 7 *********************************************************
#       THE UNITED KINGDOM
x1 = np.arange(0,626)
y1 = np.log(normalised_United_Kingdom_dataset)
plt.xticks(np.arange(0,626,15))
plt.xlim(xmin=0)
plt.xticks(rotation=90)
plt.xlabel("Days from begining of epidemic")
plt.ylabel("Number of Covid cases")
plt.title("Normalised Cumulative Covid cases of United Kingdom from 03.01.2020 to 20.09.2021")
#y2 = np.linspace(0, 626, 50)
plt.plot(x1,y1,label='The Untited Kingdom', c='m')
#plt.plot(x1,y2,label='The Untited Kingdom', c='r')
plt.legend()
plt.show()


#       ITALY
x1 = np.arange(0,626)
y1 = np.log(normalised_Italy_dataset)
plt.xticks(np.arange(0,626,15))
plt.xlim(xmin=0)
plt.xticks(rotation=90)
plt.xlabel("Days from begining of epidemic")
plt.ylabel("Number of Covid cases ")
plt.title("Normalised Cumulative Covid cases of Italy from 03.01.2020 to 20.09.2021")
plt.plot(x1,y1,label='The Untited Kingdom', c='y')
plt.legend()
plt.show()

#   UNITED STATES OF AMERICA
x1 = np.arange(0,626)
y1 = np.log(normalised_USA_dataset)
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
x1, y1 = [54.6, 102.2], [-14.73, -6.06]
plt.plot(x1, y1, '--g')
x1, y1 = [102.9, 298.9], [-6.09, -3.61]
plt.plot(x1, y1, '--r')
x1, y1 = [299, 391.8], [-3.61, -2.42]
plt.plot(x1, y1, '--g')
x1, y1 = [391.9, 613.1], [-2.43, -2.01]
plt.plot(x1, y1, '--r')

#plt.plot(x, y, '--g', label='y=2x+1')
plt.legend()
plt.show()

#************************* SLOPE-INTERCEPT**********
y1 = United_States_of_America
x1 = np.arange(0,626)
slope_intercept = np.polyfit(x1,y1,1)

print(slope_intercept)