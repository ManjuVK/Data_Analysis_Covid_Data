#%%
#                               IMPORT LIBRARIES

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
from scipy.integrate import solve_ivp
from scipy.optimize import minimize, fminbound
#%%
#                               READ DATASET
dataset = pd.read_csv("./italy data.csv")
Italy = dataset['Italy']
country = "Italy"
#%%
#******************************************* TASK 1,2 ***************************************************************
# Normalise data after removing initial data with cases <100 and plot the graph
N = 60461826
normal_data = Italy[0:]/N
data_size = len(normal_data)
x1 = np.arange(0, data_size)
plt.xticks(np.arange(0, data_size, 100))
plt.xlim(xmin=0)
# plt.xticks(rotation=90)
plt.xlabel("Days from beginning of epidemic")
plt.ylabel("Cumulative Fraction of Covid cases")
plt.title("Normalized graph of Covid cases in {}".format(country))
plt.plot(x1,normal_data, c='y')
plt.grid()
plt.show()

#%%
# #Initial conditions
R0 = 3 / N
I0 = normal_data[1]- R0
Sign = 1-I0-R0
Sres = 0
print("R0: ", R0)
print("I0: ", I0)
print("S0: ", Sign)
#%%
# # Parameter estimation & finding SLOPE 'r' AND INTERCEPT 'c'
frm = 0# 0, 20
to = 180# 20, 42 , 180
waveEnd = 180
# print ("S at start: ", (1 - normal_data[frm]))
# print ("S at End: ", (1 - normal_data[to]))
# # # #Linear regression
# Xsegmnt = np.arange(frm,to)
# Ysegment = np.log(normal_data[frm:to])
# slope_intercept = np.polyfit(Xsegmnt, Ysegment, 1)
# slope = slope_intercept[0]
# intercept = slope_intercept[1]
# b = 0.1
# a = slope+b
# print ("r: ", slope)
# print ("c: ", intercept)
# print ("a: ", a)

#play with the below values to see which gives better graph
a = 0.1222212193  #optimal a value , 1231010193
b = 0.1
k3 = 0.02
k6 = 0.01
k2 = 1

Ip = 0.02
q= k2/Ip

#%%
# --------------------------------Functions-------------------------------
t = np.arange(1, (data_size+1)) #no. of time moments
def equations(t, y):
    # y(0) = Sign(t)
    # y(1) = Sres(t)
    # y(2) = I(t)
    # y(3) = R(t)
    S_exh = 1 - np.sum(y)
    dy1 = (- a * y[0] * y[2]) - (k2 * y[0] * y[2]) + (k6 * S_exh)
    dy2 = (k2 * y[0] * y[2]) - (k3 * y[1])
    dy3 = (a * y[0] * y[2]) + (a * S_exh * y[2]) - (b * y[2])
    dy4 = b * y[2]
    return [dy1, dy2, dy3, dy4]

def equations2(t, y):
    # y(0) = Sign(t)
    # y(1) = Sres(t)
    # y(2) = I(t)
    # y(3) = R(t)
    S_exh = 1 - np.sum(y)
    dy1 = (- a * y[0] * y[2]) - (q * y[0] * (y[2]) ** 2) + (k6 * S_exh)
    dy2 = (k2 * y[0] * y[2]) - (k3 * y[1])
    dy3 = (a * y[0] * y[2]) + (a * S_exh * y[2]) - (b * y[2])
    dy4 = b * y[2]
    return [dy1, dy2, dy3, dy4]

def plotGraphs(size,cntry,yp, yn):
    plt.xticks(np.arange(0, size, 100))
    plt.xlim(xmin=0)
    plt.ylim(0.00, 0.08)
    # plt.xticks(rotation=i90)
    plt.title(" Exponential graph of Italy {}".format(a))
    plt.xlabel("Days from start of epidemic")
    plt.ylabel("Fraction of infected population")
    plt.plot(x1, yp, label="Predicted", c="r")
    plt.plot(x1, yn, label="Observed", c="y")
    plt.grid()
    plt.legend()
    plt.show()

#----------------------------------------Functions End-------------------------------------------
#%%
# # Integrate system of ODE
y0 = [Sign,Sres,I0,R0] # Initial conditions vector
ret = solve_ivp(equations, [1, data_size], y0, t_eval=t)
ypredct = ret.y[2,:] + ret.y[3,:];
Error = sum(((normal_data[0:data_size] - ypredct[0:data_size]) ** 2) / data_size)
print("Error ", Error)
plotGraphs(data_size,country,ypredct,normal_data) #plot graph

#%%
# Crowd Effect -- Integrate system of ODE
y0 = [Sign,Sres,I0,R0] # Initial conditions vector
ret = solve_ivp(equations2, [1, data_size], y0, t_eval=t)
ypredct = ret.y[2,:] + ret.y[3,:];
Error = sum(((normal_data[0:data_size] - ypredct[0:data_size]) ** 2) / data_size)
print("Error ", Error)
plotGraphs(data_size,country,ypredct,normal_data) #plot graph
