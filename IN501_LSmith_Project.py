#######################################################################
#                        Module Declarations                          #
#######################################################################
import csv;

#######################################################################
#                        Constant Declarations                        #
#######################################################################

# Constants created for readability. Instead of using index positions 
# to acces elements of the student data, constant variables names 
# correspond to column names in the file. The constant variables are 
# assigned an integer value that represent index positions of the array
STUDENT_ID = 0
FIRST_NAME = 1
LAST_NAME = 2
GRADE = 3
DEGREE = 4

#######################################################################
#                        Function Declarations                        #
#######################################################################

# Reads a file and parses file into a 2D array. Returns the 2D array
def read_file_data(filename='STUDENTDATA.txt'):
    
    # Final data structure to hold student data loaded from file
    student_data = []
    
    # Standard class to read and write files. Closes after block is 
    # executed
    with open(filename, 'r') as csvfile:
        student_data_file_reader = csv.reader(csvfile, delimiter=',')
        
        # Reads each line in the file until end of file indicator 
        for file_line in student_data_file_reader:
            
            #Creates 2D array and formats data accordint to functional requirements
            student_data_line = [int(file_line[STUDENT_ID]),file_line[FIRST_NAME],file_line[LAST_NAME],float(file_line[GRADE]),file_line[DEGREE]]
            student_data.append(student_data_line)
            
    return student_data

# Prints Main Menu Options
def print_menu():
    print('Please select a menu option (0 - 9) to perform an action:')
    print('1 - Display average grade for all students')
    print('2 - Display average grade for each program')
    print('3 - Display highest grade record')
    print('4 - Display lowest grade record')
    print('5 - Display students in MSIT')
    print('6 - Display students in MSCM')
    print('7 - Display all students in sorted order by Student ID')
    print('8 - Display invalid records')
    print('9 - Create invalid records file')
    print('0 - Exit program')

# Calculates Average Grade of Students
# Function accepts an array of data and returns the average grade
def calculate_average_grade(student_data):
    print('calculate_average_grade function called')

# Calculates Average Grade of Students by Degree
# Function accepts an array of data and returns the average grade for 
# each degree
def calculate_average_grade_by_degree(student_data):
    print('calculate_average_grade_by_degree function called')

# Gets the Highest Grade
# Function accepts an array of data and returns highest grade in the array of data
def get_highest_grade(student_data):
    print('get_highest_grade function called')

# Gets the Lowest Grade
# Function accepts an array of data and returns lowest grade in the array of data    
def get_lowest_grade(student_data):
    print('get_lowest_grade function called')

# Gets a list of students by degree
# Function accepts an array of data and degree
# Returns an array of students for a specified degree
# If no degree is given all students are returned     
def get_list_of_students_by_degree(student_data, degree='all'):
    print('get_list_of_students_by_degree function called')

# Sorts the student data by student_id field
# Function accepts an array of data and returns a sorted list of data by student_id   
def sort_students_by_student_id(student_data):
    print('sort_students_by_student_id function called')
 
# Gets a list of invilad records
# Function accepts an array of data validates data per functional requirements
# Returns a list of data that failed validation checks   
def get_invalid_records(student_data):
    print('get_invalid_records function called')

# Creates a file named 'BADRECORDS.txt'
# Function accepts an array of data and creates a file containing invalid records
# If file does not exist, a new file is created. If file exist, the existing file
# is overwritten   
def create_invalid_record_file(invalid_data):
    print('create_invalid_record_file function called')

#######################################################################
#                 Global Variable Declarations                        #
#######################################################################
student_data = []
invalid_records = []

#######################################################################
#                     Begin of Main Program                           #
#######################################################################

# Read the file and store data in global structure
student_data = read_file_data()
        
# Display Welcome message and menu to user
print('Welcome to the student data report')
print()
print_menu()

# Read and save input from user
user_menu_option = input()
print()

# Process the select menu option by the user
while (user_menu_option != '0'):
    
    # Display average grade for all students
    if user_menu_option == '1':
        calculate_average_grade(student_data)
    
    # Display average grade for each program   
    elif user_menu_option == '2':
        calculate_average_grade_by_degree(student_data)
        
    # Display highest grade record   
    elif user_menu_option == '3':
        get_highest_grade(student_data)
        
    # Display lowest grade record
    elif user_menu_option == '4':
        get_lowest_grade(student_data)
        
    # Display students in MSIT
    elif user_menu_option == '5':
        get_list_of_students_by_degree(student_data, degree='MSIT')
        
    # Display students in MSCM
    elif user_menu_option == '6':
        get_list_of_students_by_degree(student_data, degree='MSCM')
        
    # Display all students in sorted order by Student ID
    elif user_menu_option == '7':
        sort_students_by_student_id(student_data)
        
    # Display invalid records
    elif user_menu_option == '8':
        get_invalid_records(student_data)
        
    # Create invalid records file
    elif user_menu_option == '9':
        create_invalid_record_file(student_data)
        
    # Exit program
    elif user_menu_option == '0':
        print('exit program')
        continue
    
    # Invalid operation select print error message
    else:
        print(f'{user_menu_option} is an invalid choice. Try any option between 0 - 9')
    
    # Reprint menu and read and save user input
    print()
    print_menu()
    user_menu_option = input()
    print()

# Closing message 
print('Thank you for running the student data report.')
#######################################################################
#                        End of Program                               #
#######################################################################    
    