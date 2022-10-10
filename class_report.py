
"""Importing statistics to use modules for class grade stats"""


def class_report(global_data, global_file):
   '''
   This function will generate a grade report for the entire class and include calculation such as:
   Mean score, Median score, Max sore, Min score, standard deviation of the data set, and class averaqe

   @param global_data: .csv file from reader program called in main()
   @param global_file: the directory that the program main() is running in
   @return:
   '''
   os.chdir(global_file)

   data = global_data.T
   data = data[1:]



   lab_object = list(range(0, 6))
   quiz_object = list(range(6, 12))
   reading_object = list(range(12, 18))
   exams_object = list(range(18, 21))
   project_object = 21
   """These lists hold integer values that match up with the position of each assignment in the grades.csv file"""
   """This will allow for iteration"""

   num_students = 0
   final_score_list = list()
   for i, j in data.iteritems():
       """Going through data frame and using iloc[] method to grabe information based on range of assignments"""
       mean_labs = mean(list(data[i].iloc[lab_object]))
       mean_quizzes = mean(list(data[i].iloc[quiz_object]))
       mean_reading = mean(list(data[i].iloc[reading_object]))

       """seperating list of exams vs mean of exams because of different weights"""
       exams = list(data[i].iloc[exams_object])
       mean_exam = mean(exams)
       project = data[i].iloc[project_object]

       """Calulating grades based on weighted averages"""
       calculated_labs = mean_labs * 0.25
       calculated_quiz = mean_quizzes * 0.1
       calculated_reading = mean_reading * 0.1
       calculated_exam = sum([score * 0.15 for score in exams])
       calculated_project = project * 0.1

       final_score = calculated_exam + calculated_project + calculated_reading + calculated_labs + calculated_quiz
       final_score = round(final_score,2)

       """appending all final scores to a list to manipulate for class average and standard deviation"""
       final_score_list.append(final_score)
       num_students += 1

   with open(f"Class_report.txt", "w+") as class_report_card:
       '''
       Opening a new class report txt file and then writing the stats to the file
       Opend as 'w+' to create new file if not existing and to re-write in case of grade.csv changes
       '''
       class_report_card.write(f"Total number of students: {num_students}\n")
       class_report_card.write(f"Minimum score: {round(min(final_score_list),1)}\n")
       class_report_card.write(f"Maximum score {round(max(final_score_list),1)}\n")
       class_report_card.write(f"Median score: {round(median(final_score_list),1)}\n")
       class_report_card.write(f"Mean score: {round(mean(final_score_list),1)}\n")
       class_report_card.write(f"Standard deviation: {round(stdev(final_score_list),1)}\n")

   return


