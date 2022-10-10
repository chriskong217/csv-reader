
def student_report_file(global_data, global_file):
    '''
       This function will generate a grade report for a specified student based on their UIN
       It will then create and write to a new file named (uin).txt with the students grade statistics

       @param global_data: .csv file from reader program called in main()
       @param global_file: the directory that the program main() is running in
       @return:
    '''
    os.chdir(global_file)
    data = global_data
    uin_list = list(data.loc[:, 'UIN'])
    """checking validity of the UIN"""
    Valid_uin = False
    while Valid_uin == False:
        try:
            uin = input("Enter Student UIN: ")
            if len(uin) == 10:
                uin = int(uin)
                if uin in uin_list:
                    Valid_uin = True
                    print(f"UIN {uin} found in gradebook")
                    print(f"Generating grade report for student {uin}")
                    uin_position = uin_list.index(uin)
                else:
                    print("Invalid UIN\n")
            else:
                print("Invalid UIN\n")
        except Exception as e:
            print(e)

    """Now going to traverse the csv file to grab grades according to UIN"""
    lab_object = list(range(1, 7))
    quiz_object = list(range(7, 13))
    reading_object = list(range(13, 19))
    exams_object = list(range(19, 22))
    project_object = 22

    """Grabbing scores based on the index of the UIN found earlier; row is UIN, column is assignment scores"""
    lab_scores = dict(data.iloc[uin_position, lab_object])
    quiz_scores = dict(data.iloc[uin_position, quiz_object])
    reading_scores = dict(data.iloc[uin_position, reading_object])
    exam_scores = dict(data.iloc[uin_position, exams_object])
    project_scores = data.iloc[uin_position, 22]

    """Calculating averages of all scores"""
    lab_mean = round((sum(lab_scores.values()) / len(lab_scores)), 1)
    quiz_mean = round((sum(quiz_scores.values()) / len(quiz_scores)), 1)
    reading_mean = round((sum(reading_scores.values()) / len(reading_scores)), 1)
    exam_mean = round(sum(exam_scores.values()) / len(exam_scores), 1)
    project_mean = project_scores

    """Calculated final scores with the weighted averages"""
    final_exam_grade = round(sum([score * 0.15 for score in exam_scores.values()]), 1)
    final_course_grade = project_mean * 0.1 + final_exam_grade + reading_mean * 0.1 + quiz_mean * 0.1 + lab_mean * 0.25
    temp = final_course_grade
    final_course_grade = round(temp, 2)

    letter_grade = ""

    if 90 <= final_course_grade <= 110:
        letter_grade = "A"
    elif 80 <= final_course_grade < 90:
        letter_grade = "B"
    elif 70 <= final_course_grade < 80:
        letter_grade = "C"
    elif 60 <= final_course_grade < 70:
        letter_grade = "D"
    elif final_course_grade < 60:
        letter_grade = "F"

    """Writing information to a new file"""
    with open(f"{uin}.txt", "w+") as student_report_card:
        student_report_card.write(f"Exams mean: {exam_mean}\n")
        student_report_card.write(f"Labs mean: {lab_mean}\n")
        student_report_card.write(f"Quizzes mean: {quiz_mean}\n")
        student_report_card.write(f"Reading Activities mean: {reading_mean}\n")
        student_report_card.write(f"Score: {final_course_grade}\n")
        student_report_card.write(f"Letter Grade: {letter_grade}\n")






