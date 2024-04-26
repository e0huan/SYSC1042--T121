#Elaine Huang
#Mohammad Abu Hammad
#Camden Erwin
#Brandon Wu

from T121_M1_load_data import *
from T121_M2_sort_plot import *
from T121_M2_student_list import *
from T121_M3_optimization import *

supported_operations = {'L', 'S', 'H', 'W', 'B', 'Q', 'l', 's', 'h', 'w', 'b', 'q'}
    
def text_ui():
    """User interface for calling upon and organizing data files.
    
    User should only input supported operations.
    """
    loop = 1
    
    while loop == 1:
        command = input("The available commands are: 1. L)oad Data 2. S)ort Data 3. H)istogram 4. W)orst _____ for Grades 5. B)est _____ for Grades 6. Q)uit Please type your command:<one space>")
        
        if command not in supported_operations:
            print("No such command")
        elif command == 'L' or command == 'l':
            filename = input("Please enter the name of the file:")
            key = input("Please enter the attribute to use as key:")
            data = add_average(load_data(filename, key))
            print("Data loaded")
            loop = 2
        else:
            print("File not loaded. Please, load a file first.")
    
    while loop == 2:
        command = input("The available commands are: 1. L)oad Data 2. S)ort Data 3. H)istogram 4. W)orst _____ for Grades 5. B)est _____ for Grades 6. Q)uit Please type your command:<one space>")
        
        if command == 'L' or command == 'l':
            filename = input("Please enter the name of the file:")
            key = input("Please enter the attribute to use as key:")
            data = add_average(load_data(filename, key))
            print("Data loaded")
        elif command == 'S' or command == 's':
            attribute = input("Please enter the attribute you want to use for sorting: 'School' 'Age' 'StudyTime' 'Failures' 'Health' 'Absences' 'G1' 'G2' 'G3' 'G_Avg':")
            sorted_data = sort_student_bubble(data, attribute)
            display = input("Data Sorted. Do you want to display the data?:")
            if display == "Y":
                print(sorted_data)
        elif command == 'H' or command == 'h':
            attribute = input("Please enter the attribute you want to use for histogram: 'School' 'Age' 'StudyTime' 'Failures' 'Health' 'Absences' 'G1' 'G2' 'G3' 'G_Avg':")
            hist = histogram(data, attribute)
            display = input("Histogram created. Do you want to display the Histogram?:")
            if display == "Y":
                print(hist)
        elif command == 'W' or command == 'w':
            attribute = input("Please enter the attribute you want to calculate the worse value of the attribute for in terms of grades: 'Age' 'StudyTime' 'Failures' 'Health' 'Absences'")
            worst = minimum(data, attribute)
            print("The worst value for the attribute {0} is {1}".format(attribute, worst))
        elif command == 'B' or command == 'b':
            attribute = input("Please enter the attribute you want to calculate the best value of the attribute for in terms of grades: 'Age' 'StudyTime' 'Failures' 'Health' 'Absences'")
            best = maximum(data, attribute)
            print("The best value for the attribute {0} is {1}".format(attribute, best))
        elif command == 'Q' or command == 'q':
            print("Quitting")
            loop = 3
        else:
            print("Invalid command")

print(text_ui())
