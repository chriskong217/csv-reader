

def print_menu():
   '''Prints the option menu
   :return:
   '''
   print("*******************Main Menu*****************")
   print("1. Read CSV file of grades")
   print("2. Generate student report file")
   print("3. Generate student report charts")
   print("4. Generate class report file")
   print("5. Generate class report charts")
   print("6. Quit")
   print("************************************************")

def main():
   '''
   Asks for user input for options until user enters quit, executes user inputted options by calling various functions
   :return:
   '''
   """Establishes initial directory"""
   local_file = os.getcwd()
   """Isolates the directory the program is initially present in and sets it as a global variable"""
   global global_file
   global_file = local_file
   while True:
       try:
           print_menu()
           option = input()
           if option.lower() == 'quit':
               break
           if option.lower() == 'q':
               break
           elif int(option) == 1:
               file_name = input("Input file name: ")
               """Reads file using pandas and inputs user input as file name"""
               data = reader.read_file(file_name)
               """Sets the data as a global variable"""
               global global_data
               global_data = data
           elif int(option) == 2:
               srf.student_report_file(global_data, global_file)
           elif int(option) == 3:
               """Inputs data from option 1 and initial directory into bar, which reads the data and produces bar charts"""
               bar.bar_chart(global_data, global_file)
               pass
           elif int(option) == 4:
               cr.class_report(global_data, global_file)
           elif int(option) == 5:
               """Inputs data from option 1 and initial directory into charts, which reads the data and produces graphs"""
               charts.class_chart(global_data, global_file)
       except NameError:
           print("Please select option 1 before starting")




if __name__ == '__main__':
   main()

