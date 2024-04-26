#Elaine Huang
#Mohammad Abu Hammad
#Camden Erwin
#Brandon Wu

import numpy as np
import matplotlib.pyplot as plt
from T121_M1_load_data import *

def student_list(dictionary: dict)-> list:
    """Takes a dictionary and converts all the data into a list
    
    >>> student_list(load_data(('student-mat.csv', 'Age'))
    [{' School': 'GP', 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6, 'Age': '18'}, ...
    """    
    new_list = []
    values = dictionary.values()
    
    missing_key = ''

    for vals in values: 
        new_list += vals
    
    if ' School' not in new_list[0].keys():
        missing_key = 'School'
    elif 'Age' not in new_list[0].keys():
        missing_key = 'Age'
    elif 'Health' not in new_list[0].keys():
        missing_key = 'Health'
    elif 'Failures' not in new_list[0].keys():
        missing_key = 'Failures' 
        
        
    students_list = []
    for key in dictionary.keys():
        student = dictionary.get(key)
        for i in range(len(student)):
            student[i][missing_key] = key
        students_list += student
          
    return students_list



#Mohammad Abu Hammad #101280485

def sort_student_bubble(dictionary: dict, attribution: str):

    """Function uses the bubble sort algorithim in order to sort an inputed

    dictionary (that is converted to a list with the student_list function)

    based on the input parameter attribution.

 

    Precondition: None

 

    Examples

    >>>sort_student_bubble(add_average(load_data('student-mat.csv', 'School')), 'Age')

 

    """

    pass

 

    temp_dict = student_list(dictionary)

    swap = True

    while swap:

        swap = False

        for i in range(len(temp_dict) - 1):

            if type(temp_dict[i].get(attribution)) is int or type(temp_dict[i].get(attribution)) is float:

                if temp_dict[i].get(attribution) > temp_dict[i + 1].get(attribution):

                    swap = True

            elif type(temp_dict[i].get(attribution)) is str:

                if temp_dict[i].get(attribution).lower() > temp_dict[i + 1].get(attribution).lower():

                    swap = True

            if swap:

                temp_dict[i], temp_dict[i + 1] = temp_dict[i + 1], temp_dict[i]

    return temp_dict

 

#X = load_data('student-mat.csv', 'School')

d = sort_student_bubble(add_average(load_data('student-mat.csv', 'School')), 'Failures')

print(d)



"""
Elaine Huang 101273300

[{' School': 'MS', 'Age': '17', 'StudyTime': '1', 'Failures': '0', 'Absences': '3', 'G1': '14', 'G2': '16', 'G3': '16', 'Health': '2'}...{' School': 'GP', 'Age': '15', 'StudyTime': '3', 'Failures': '0', 'Absences': '2', 'G1': '15', 'G2': '14', 'G3': '15', 'Health': '5'}]

The function returns a dictionary which is sorted either alphebetically or from increasing order depending on the called attribute
The parameter student_n_dictionary is any dictionary existing in the load data function and the key parameter is the attribute that is to be sorted by

"""


def selection_sort(student_n_dictionary:dict, key:str)->dict:
    
    nlist = student_list(student_n_dictionary)
        
    for i in range(len(nlist)):
        min_i = i
        min_idict=nlist[min_i][key]
        for j in range(i+1, (len(nlist))):
            jdict = nlist[j][key]
            if min_idict > jdict:
                min_i=j
        nlist[i], nlist[min_i]=nlist[min_i], nlist[i]
    return nlist



def curve_fit(dictionary:dict, attribute:str, degree: int):
    avg = add_average(dictionary)
    n=student_list(avg)
    al=[]
    gl=[]
    sgl=[]
    aset=set()
    tempdict={}
    als=[]
    
    for i in n:
        a=i[attribute]
        al.append(a)
        g=i["G_Avg"]
        gl.append(g)
        aset.add(a)
        als.append(a)
        gls=copy.deepcopy(gl)   
    for p in aset:
        count=0
        arg=0
        for n in al:   
            if n==p:
                l=als.index(n)
                als.remove(n)
                count+=1
                r=gls[l]
                arg+=r
                rv=arg/count
                gls.pop(l)
                tempdict[n]=rv
    x=[]
    y=[]
    for q in tempdict.keys():
        x.append(q)
    for w in tempdict.values():
        y.append(w)
    minx=x[0]
    maxx=x[-1]
    z=np.polyfit(x,y,degree)
    plt.scatter(x,y)
    plt.show()
    if len(x)>degree+1:#interpolations
        newd = degree
    else:
        newd = len(x)-11#regression
    z = np.polyfit(x, y, newd)    
    return(minx, maxx, z)
        
        #for each attribute calculate the average of the average
    

   
s = student_school_dictionary("student-mat.csv")
    
a = student_age_dictionary("student-mat.csv")
    
h = student_health_dictionary("student-mat.csv")
    
f = student_failures_dictionary("student-mat.csv")
    
    
def histogram(dictionary: str, key: str) -> dict:
    student_list("student-mat.csv")
    if key == "age":
        for key, val in sorted(a.items()):
            student_list[val].append(key)
            plt.hist((str(dict(student_list))), bins=10)
            plt.show()
    elif key == "school":
        for key, val in sorted(s.items()):
            student_list[val].append(key)
            plt.hist((str(dict(student_list))), bins=10)
            plt.show()
    elif key == "health":
        for key, val in sorted(h.items()):
            student_list[val].append(key)
            plt.hist((str(dict(student_list))), bins=10)
            plt.show()
    elif key == "failures":
        for key, val in sorted(f.items()):
            student_list[val].append(key)
            plt.hist((str(dict(student_list))), bins=10)
            plt.show()

