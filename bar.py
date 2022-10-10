
def bar_chart(global_data, global_file):
   '''Creates bar chart of individual students from csv data

   Retrieves data from global variable global_data and analyzes it to create bar charts of specific students
   based on user inputted UINs.

   :param global_data:
       .csv file from reader program called in main()
   :param global_file:
       the directory that the program main() is running in
   :return:
   '''
   """Sets data equal to global_data, which is the read data file from option 1"""
   data = global_data
   student_uin = float(input("Enter Student UIN: "))
   try:
       """Resets the directory path to initial directory the entire program is running in"""
       os.chdir(global_file)
       """Creates directory with name of student id and sets the directory path to it"""
       os.mkdir(str(int(student_uin)))
       os.chdir(str(int(student_uin)))
   except KeyError as e:
       print("e")
   '''LAB BAR GRAPH'''
   """Creates bar graph for each inputted student UIN's labs"""
   """Limits the dataset to just the labs"""
   shortened2 = data.iloc[:, 0:7]
   """Transposes the limited dataset"""
   data_t = shortened2.T
   """Sets the header to be the first row of the transposed dataset"""
   new_header = data_t.iloc[0]
   data_t = data_t[1:]
   data_t.columns = new_header
   """Creates bar graph of the column where the inputted student UIN is the header"""
   graph = data_t[int(student_uin)]
   graph.plot(kind="bar", rot=0)
   plt.title(f"Lab grades for {int(student_uin)}")
   plt.xlabel("Lab #")
   plt.ylabel("Score(%)")
   """Saves the bar graph as a png into the before created directory with the student UIN as name"""
   plt.savefig("labs.png", bbox_inches="tight")
   plt.show()
   '''QUIZZES BAR GRAPH'''
   """Creates bar graph for each inputted student UIN's quizzes"""
   """Limits the dataset to just the quizzes"""
   shortened3 = data.iloc[:, [0, 7, 8, 9, 10, 11, 12]]
   """Transposes the limited dataset"""
   data_t2 = shortened3.T
   """Sets the header to be the first row of the transposed dataset"""
   new_header2 = data_t2.iloc[0]
   data_t2 = data_t2[1:]
   data_t2.columns = new_header2
   """Creates bar graph of the column where the inputted student UIN is the header"""
   graph2 = data_t2[int(student_uin)]
   """Plots the bar graph and adds labels"""
   graph2.plot(kind="bar", rot=0)
   plt.title(f"Quiz grades for {int(student_uin)}")
   plt.xlabel("Quiz #")
   plt.ylabel("Score(%)")
   """Saves the bar graph as a png into the before created directory with the student UIN as name"""
   plt.savefig("quizzes.png", bbox_inches="tight")
   plt.show()
   '''READING ACTIVITIES BAR GRAPH'''
   """Creates bar graph for each inputted student UIN's reading activities"""
   """Limits the dataset to just the reading activities"""
   shortened4 = data.iloc[:, [0, 13, 14, 15, 16, 17, 18]]
   """Transposes the limited dataset"""
   data_t3 = shortened4.T
   """Sets the header to be the first row of the transposed dataset"""
   new_header3 = data_t3.iloc[0]
   data_t3 = data_t3[1:]
   data_t3.columns = new_header3
   """Creates bar graph of the column where the inputted student UIN is the header"""
   graph3 = data_t3[int(student_uin)]
   """Plots the bar graph and adds labels"""
   graph3.plot(kind="bar", rot=0)
   plt.title(f"Reading Activity grades for {int(student_uin)}")
   plt.xlabel("Reading Activity #")
   plt.ylabel("Score(%)")
   """Saves the bar graph as a png into the before created directory with the student UIN as name"""
   plt.savefig("readings.png", bbox_inches="tight")
   plt.show()
   '''EXAMS BAR GRAPH'''
   """Creates bar graph for each inputted student UIN's exams"""
   """Limits the dataset to just the exams"""
   shortened5 = data.iloc[:, [0, 19, 20, 21]]
   """Transposes the limited dataset"""
   data_t4 = shortened5.T
   """Sets the header to be the first row of the transposed dataset"""
   new_header4 = data_t4.iloc[0]
   data_t4 = data_t4[1:]
   data_t4.columns = new_header4
   """Creates bar graph of the column where the inputted student UIN is the header"""
   graph4 = data_t4[int(student_uin)]
   """Plots the bar graph and adds labels"""
   graph4.plot(kind="bar", rot=0)
   plt.title(f"Exam grades for {int(student_uin)}")
   plt.xlabel("Exam #")
   plt.ylabel("Score(%)")
   """Saves the bar graph as a png into the before created directory with the student UIN as name"""
   plt.savefig("exams.png", bbox_inches="tight")
   plt.show()





