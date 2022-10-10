

def class_chart(global_data, global_file):
   '''Creates a pie chart and a bar chart analyzing the class distribution information from the
   user inputted csv file

   :param global_data:
       .csv file from reader program called in main()
   :param global_file:
       the directory that the program main() is running in
   :return:
   '''
   """Sets data equal to global_data, which is the read data file from option 1"""
   data = global_data
   try:
       """Resets the directory path to initial directory the entire program is running in"""
       os.chdir(global_file)
       """Creates directory with name of class_charts and sets the directory path to it"""
       os.mkdir('class_charts')
       os.chdir('class_charts')
   except Exception as e:
       print(e)
   """Creates the int letter grade variables to track how many of each letter grade there is later on"""
   a = 0
   b = 0
   c = 0
   d = 0
   f = 0
   """Transposes the data and sets the first row in the transposed data as the header"""
   data_t = data.T
   new_header = data_t.iloc[0]
   data_t = data_t[1:]
   data_t.columns = new_header
   """Iterates through each column in the data set"""
   for (columnName, columnData) in data_t.iteritems():
       """Goes through the only labs in the columns and takes the average"""
       lab_average = data_t[columnName].iloc[[0, 1, 2, 3, 4, 5]].mean()
       """Multiplies the lab average by 0.25"""
       lab_calculated = lab_average*0.25
       """Goes through the only quizzes in the columns and takes the average"""
       quiz_average = data_t[columnName].iloc[[6, 7, 8, 9, 10, 11]].mean()
       """Multiplies the quiz average by 0.1"""
       quiz_calculated = quiz_average*0.1
       """Goes through only the reading averages in the column and takes the average"""
       reading_average = data_t[columnName].iloc[[12, 13, 14, 15, 16, 17]].mean()
       """Multiplies the reading average by 0.1"""
       reading_calculated = reading_average*0.1
       """Isolates the exam 1 grade in the column"""
       exam1 = data_t[columnName].iloc[[18]].mean()
       """Multiplies the grade by 0.15"""
       exam1_calculated = exam1*0.15
       """Isolates the exam 2 grade in the column"""
       exam2 = data_t[columnName].iloc[[19]].mean()
       """Multiplies the grade by 0.15"""
       exam2_calculated = exam2 * 0.15
       """Isolates the exam 3 grade in the column"""
       exam3 = data_t[columnName].iloc[[20]].mean()
       """Multiplies the grade by 0.15"""
       exam3_calculated = exam3 * 0.15
       """Isolates the project grade in the column"""
       project = data_t[columnName].iloc[[21]].mean()
       """Multiplies the grade by 0.1"""
       project_calculated = project * 0.1
       """Adds up all the multiplied averages to get total score"""
       total_grade = lab_calculated + quiz_calculated + reading_calculated + exam1_calculated + exam2_calculated + exam3_calculated + project_calculated
       """Adds 1 to the count of each variable when the parameters for the letter grade are met"""
       if 90 <= round(total_grade, 2) <= 110:
           a += 1
       elif 80 <= round(total_grade, 2) <= 89:
           b += 1
       elif 70 <= round(total_grade, 2) <= 79:
           c += 1
       elif 60 <= round(total_grade, 2) <= 69:
           d += 1
       elif round(total_grade, 2) < 60:
           f += 1
   """Establishes list of string of letter grade"""
   letter_grade = ["A", "B", "C", "D", "F"]
   """Establishes list of the variables containing the count of each letter grade"""
   num_grades = [a, b, c, d, f]
   """Creates the pi chart"""
   pi_chart = plt.figure(figsize=(10, 7))
   plt.pie(num_grades, labels=letter_grade)
   plt.title("Class letter grades")
   plt.savefig("pi_chart")
   plt.show()
   """Creates a data frame from the list of letter grade strings and the list of the variables containing the count
   letter grades"""
   grade_bar = pd.DataFrame({'grade': letter_grade, 'value': num_grades})
   """Plots the made data frame as a bar chart"""
   grade_bar.plot.bar(x='grade', y='value', rot=0, legend=False)
   plt.xlabel("Grade")
   plt.ylabel("Count")
   plt.title("Class letter grades")
   plt.savefig("bar_chart")
   plt.show()


