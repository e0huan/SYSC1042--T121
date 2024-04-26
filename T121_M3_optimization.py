#Elaine Huang
#Mohammad Abu Hammad
#Camden Erwin
#Brandon Wu

import numpy as np
from scipy.optimize import fminbound, fsolve
from T122_M1_Load_Data import *
from T122_M2_curve_fit import *
import copy
import matplotlib.pyplot as plt

 

 

def f(x: float, equation: list) -> float:

    return np.polyval(equation, x)

 

 

def minimum(data: dict, attribute: str) -> float:

    """

     This function is used to find which attribute level is the worst in termsof grades.

     The function takes a dictionary and a string (attribute) as a parameter and returns a tuple containing

     the x and y value of the local minimum between the lowest and highest value of the attribute.

 

     minimum(add_average(load_data("student-mat.csv","health")),"Age")

 

    """

    eq, interval = curve_fit(data, attribute, 1)

    Max, Min = interval

    optimize = fminbound(f, Min, Max, args=(eq,))

 

    return (optimize, round(f(optimize, eq), 2))

 

 

def minus_f(x: float, equation: list) -> float:

    return -f(x, equation)


def f_minus(x):
    return -curve_fit(curve_fit.z, x)
def maximum(dictionary:dict, attribute:str)->tuple:
    tup = ()
    avg = add_average(dictionary)
    n=student_list(avg)
    c=curve_fit(n,attribute,degree)
    xmax= fminbound(f_minus, curve_fit.minx, curve_fit.maxx)
    ymax=curve_fit(curve_fit.z,xmax)
    plt.figure()
    plt.plot([xmax],[ymax],x,y)
    plt.show
