#Elaine Huang
#Mohammad Abu Hammad
#Camden Erwin
#Brandon Wu


import string
from typing import List
from check_equal import *

def student_school_dictionary(filename: str) -> dict:
    
    infile = open(filename, "r")
    count = 0
    student_school_dictionary = {}
    
    for line in infile:
        
        data = line.strip('\n').split(',')
        if count == 0:
            header = data
        else:
            if not (data[0]) in (student_school_dictionary):
                student_school_dictionary[data[0]] = []
            temp_dict = {}
            temp_dict[header[1]] = int(data[1])
            temp_dict[header[2]] = int(data[2])
            temp_dict[header[3]] = int(data[3])
            temp_dict[header[4]] = int(data[4])
            temp_dict[header[5]] = int(data[5])
            temp_dict[header[6]] = int(data[6])
            temp_dict[header[7]] = int(data[7])
            temp_dict[header[8]] = int(data[8])
                
            student_school_dictionary[data[0]].append(temp_dict)
            
        count += 1
        
    infile.close()
    
    return student_school_dictionary




def student_health_dictionary(filename: str) -> dict: 
    """ 
    The keys of the dictionary are the students' health numbers. 
A student's health range is from 1 (meaning very bad) to 5 (meaning very good). 
See below for the sample output of the function: 

{ 1 : [ {'School':'GP', 'Age': 17, 'StudyTime': 4.2, 'Failures': 3, 
'Absences': 6, 'G1': 7, 'G2': 8, 'G3': 10 }, 
{another element}, 
… ], 

2 : [ {'School': 'MS', 'Age': 20, 'StudyTime': 1.2, 'Failures': 1, 
'Absences': 10, 'G1': 9, 'G2': 11, 'G3': 7}, 
{another element}, 
… ], 
… } 
   """ 
    x = open(filename, 'r') 

    count = 0  

    student_health_dictionary = {} 

    for line in x:  

        data = line.strip('\n').split(',') 
        if count == 0: 
            header = data  
            
        else: 
            if not (data[4]) in (student_health_dictionary): 

                student_health_dictionary[data[4]] = [] 

            temp_dict = {} 
            temp_dict[header[0]] = (data[0]) 
            temp_dict[header[1]] = (data[1]) 
            temp_dict[header[2]] = (data[2]) 
            temp_dict[header[3]] = (data[3]) 
            temp_dict[header[5]] = (data[5]) 
            temp_dict[header[6]] = (data[6]) 
            temp_dict[header[7]] = (data[7]) 
            temp_dict[header[8]] = (data[8]) 

            student_health_dictionary[data[4]].append(temp_dict) 

        count += 1 

    x.close() 
    
    return student_health_dictionary 

word_list = student_health_dictionary('student-mat.csv') 





def student_age_dictionary(filename: str) -> dict:
    """return a dictionary of all the student's data with their age as the dictionary key, given a csv file.
    
    >>>  student_age_dictionary('student-mat.csv')
    {'18': [{' School': 'GP', 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, ...}
    """
    
    infile = open(filename, "r")
    count = 0
    student_age_dictionary = {}
    
    for line in infile:
        
        data = line.strip('\n').split(',')
        if count == 0:
            header = data
        else:
            if not (data[1]) in (student_age_dictionary):
                student_age_dictionary[data[1]] = []
            temp_dict = {}
            temp_dict[header[0]] = (data[0])
            temp_dict[header[2]] = int(data[2])
            temp_dict[header[3]] = int(data[3])
            temp_dict[header[4]] = int(data[4])
            temp_dict[header[5]] = int(data[5])
            temp_dict[header[6]] = int(data[6])
            temp_dict[header[7]] = int(data[7])
            temp_dict[header[8]] = int(data[8])
                
            student_age_dictionary[data[1]].append(temp_dict)
            
        count += 1
        
    infile.close()
    
    return student_age_dictionary




def student_failures_dictionary(filename) -> dict:
    file_in = open("student-mat.csv")
    header = file_in.readline()
    headerlist = []
    student_failures_dictionary = {}
    headerlist = header.strip("\n").split(",")

    for line in file_in:
        data_list = line.strip("\n").split(",")

        if not (data_list[3]) in student_failures_dictionary:
            student_failures_dictionary[data_list[3]] = []
        temp_dict = {}
        temp_dict[headerlist[0]] = (data_list[0])
        temp_dict[headerlist[1]] = int(data_list[1])
        temp_dict[headerlist[2]] = int(data_list[2])
        temp_dict[headerlist[4]] = int(data_list[4])
        temp_dict[headerlist[5]] = int(data_list[5])
        temp_dict[headerlist[6]] = int(data_list[6])
        temp_dict[headerlist[7]] = int(data_list[7])
        temp_dict[headerlist[8]] = int(data_list[8])

        student_failures_dictionary[data_list[3]].append(temp_dict)

    file_in.close()
    return student_failures_dictionary




def load_data(filename: str, key: str) -> dict:
    if key == 'School':
        return student_school_dictionary(filename)
    elif key == 'Age':
        return student_age_dictionary(filename)
    elif key == 'Health':
        return student_health_dictionary(filename)
    elif key == 'Failures':
        return student_failures_dictionary(filename)
    else:
        print("Invalid Key")
        

def add_average(student_n_dictionary: dict) -> dict:
    data = student_n_dictionary
    for value in data.values():
        i = 0
        for i in range (len(value)):
            tempsdict={}
            tempsdict=(value[i])
            new_list=list(tempsdict.values())
            average = (int(new_list[5])+int(new_list[6])+int(new_list[7]))/3
            i+=1
            tempsdict['G_Avg']=round(average,2)
    return data

def student_list(dictionary: dict)-> list:
        
    new_list = []
    values = dictionary.values()
    print(values)
    
    
    missing_key = ''

    for vals in values: 
        new_list += vals
    
    if 'School' not in new_list[0].keys():
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


#Test 1
s = student_school_dictionary("student-mat.csv")
            
a = student_age_dictionary("student-mat.csv")
            
h = student_health_dictionary("student-mat.csv")
            
f = student_failures_dictionary("student-mat.csv")
        
if s.keys() == {'GP', 'MB', 'CF', 'BD', 'MS'}:
    print("passed")
if a.keys() == {"15", "16", "17", "18", "19", "20", "21", "22"}:
    print("passed")
if h.keys() == {"1", "2", "3", "4", "5"}:
    print("passed")
if f.keys() == {"0", "1", "2", "3"}:
    print("passed")
else:
    print("failed")
        
        
#Test 2
if len(s) == 5:
    print("passed")
else:
    print("failed")
        
if len(a) == 8:
    print("passed")
else:
    print("failed")
            
if len(h) == 5:
    print("passed")
else:
    print("failed")
        
if len(f) == 4:
    print("passed")
else:
    print("failed")


#Test 3
import unittest

class Test_Lab4 (unittest.TestCase):

    def test_dictionary_values_individual_student_entries (self):

        """

This test checks that each individual student entry in the dictionary is stored

correctly. The format for a student's data is: {'School': 'MS', 'Age':'17',

'StudyTime': 2.5, 'Failures': 3, 'Health': 3,'Absences': 2, 'GI': 8,'G2': 8,

'G3': 101. This format is checked for each student in the dictionary.

"""

        for i in range(4):

            student_dict = load_data(i)

            for key, value in student_dict.items ():

                if key == 0:

                    self.assertEqual (value, {'School':'MS', 'Age': '17',

                                    'StudyTime': 2.5, 'Failures': 3, 'Health': 3,

                                    'Absences': 2, 'G1': 8, 'G2': 8, 'G3': 10 })

                if key == 1:

                    self.assertEqual (value, {'School':'MS', 'Age': '16',

                                    'StudyTime': 2, 'Failures': 3,'Health': 3,

                                    'Absences': 0, 'G1': 0, 'G2': 0, 'G3': 0})

                if key == 2:self.assertEqual (value, {'School':'MS', 'Age': '16',

                                            'StudyTime': 2, 'Failures': 3,

                                            'Health': 3, 'Absences': 0, 'G1': 0,

                                            'G2': 0, 'G3': 0 })

                if key == 3:

                    self.assertEqual (value, {'School':'MS', 'Age': '16',

                                    'StudyTime': 2,'Failures': 3,'Health': 3,

                                    'Absences': 0, 'GI': 0, 'G2': 0,'G3': 0})

                if key == 4:

                    self.assertEqual (value, {'School':'MS', 'Age': '17',

                                    'StudyTime': 2.5,'Failures': 3,'Health': 3,

                                    'Absences': 2, 'GI': 8, 'G2': 8,'G3': 10})

if __name__ == '__main__':

    print('Running unit tests')

    unittest.main()


#Test 4
#Part 1   
if __name__ == '__main__':
    
    #student_school_dictionary
    grades = add_average(s)
    #This is the count for students in the original set before adding G_Avg
    students = 0
    #This is the count for students after adding the G_Avg
    student_avg = 0
    
    for key in s:
        #This is the amount of students in the original set before adding G_Avg
        students += len(s[key])
        
    for key in grades:
        #This is the amount of students after adding the G_Avg
        student_avg += len(grades[key])
    
    print(students == student_avg)
    
    #student_health_dictionary
    grades = add_average(h)
    students = 0
    student_avg = 0
    
    for key in h:
        students += len(h[key])
        
    for key in grades:
        student_avg += len(grades[key])
    
    print(students == student_avg)
    
    #student_age_dictionary
    grades = add_average(a)
    students = 0
    student_avg = 0
    
    for key in a:
        students += len(a[key])
        
    for key in grades:
        student_avg += len(grades[key])
    
    print(students == student_avg)   
    
    #student_failures_dictionary
    grades = add_average(f)
    students = 0
    student_avg = 0
    
    for key in f:
        students += len(f[key])
        
    for key in grades:
        student_avg += len(grades[key])
    
    print(students == student_avg)
    
    
    #Part 2
    
    #student_school_dictionary
    avg = ''
    g_avg = add_average(s)
    for value in g_avg.values():
        i = 0
        for i in range (len(value)):
            tempsdict={}
            tempsdict=(value[i])
            new_list=list(tempsdict.keys())
            avg = new_list[8]
    print('G_Avg' == avg)    
    #student_health_dictionary
    avg = ''
    g_avg = add_average(h)
    for value in g_avg.values():
        i = 0
        for i in range (len(value)):
            tempsdict={}
            tempsdict=(value[i])
            new_list=list(tempsdict.keys())
            avg = new_list[8]
    print('G_Avg' == avg)    
    #student_age_dictionary
    avg = ''
    g_avg = add_average(a)
    for value in g_avg.values():
        i = 0
        for i in range (len(value)):
            tempsdict={}
            tempsdict=(value[i])
            new_list=list(tempsdict.keys())
            avg = new_list[8]
    print('G_Avg' == avg)    
    #student_failure_dictionary
    avg = ''
    g_avg = add_average(f)
    for value in g_avg.values():
        i = 0
        for i in range (len(value)):
            tempsdict={}
            tempsdict=(value[i])
            new_list=list(tempsdict.keys())
            avg = new_list[8]
    print('G_Avg' == avg)
        
    #Part 3
    #student_school_dictionary
    average = add_average(s)
    rand_val = average['GP'][0]
    avg_val=rand_val['G_Avg']
    #5.67 is manually calculated; {'GP': [{'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}; (5+6+6)/3=5.67 (when rounded to 2 decimal places)
    print(5.67==avg_val)
    
    #student_health_dictionary
    average = add_average(h)
    rand_val = average['5'][1]
    avg_val=rand_val['G_Avg']
    #8.67 is manually calculated; {'5': [{...}, {' School': 'GP', 'Age': '16', 'StudyTime': '2', 'Failures': '0', 'Absences': '4', 'G1': '6', 'G2': '10', 'G3': '10'}; (6+10+10)/3=8.67 (when rounded to 2 decimal places)
    print(8.67==avg_val)   
    
    #student_age_dictionary
    average = add_average(a)
    rand_val = average['19'][4]
    avg_val=rand_val['G_Avg']
    #9.00 is manually calculated; {'19': [{...}, {...}, {...}, {...}, {' School': 'BD', 'StudyTime': 2, 'Failures': 2, 'Health': 5, 'Absences': 15, 'G1': 9, 'G2': 9, 'G3': 9}; (9+9+9)/3=9.00 (when rounded to 2 decimal places)
    print(9.0==avg_val)    
    
    #student_failure_dictionary
    average = add_average(f)
    rand_val = average[3][0]
    avg_val=rand_val['G_Avg']
    #8.33 is manually calculated;  3: [{' School': 'GP', 'Age': 15, 'StudyTime': 2, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}; (7+8+10)/3=8.33 (when rounded to 2 decimal places)
    print(8.33==avg_val)    