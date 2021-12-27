import csv

def read_file(line_len, file_name):
    f = open(f"text/{file_name}", mode = "r", encoding = "utf-8")
    text = f.readlines()
    seperated_text = []
    for line in text:
        line = line.strip("\n")
        if len(line) < line_len:
            seperated_text.append(line)
        else:
            for i in range(len(line)//line_len + 1):
                if i == len(line)//line_len + 1:
                    seperated_text.append(line[(line_len * i)::])
                else:
                    seperated_text.append(line[(line_len * i):(line_len * (i+1))])
        seperated_text.append("\n")
    f.close()
    return seperated_text


def read_course():
    f = open("text/course.csv", mode = "r", encoding = "utf-8")
    csvReader = csv.reader(f)
    course_list = list(csvReader)
    for i in range(len(course_list)):
        if course_list[i][0] != "課程":
            course_list[i][2] = int(course_list[i][2])
            course_list[i][3] = int(course_list[i][3])
            course_list[i][4] = int(course_list[i][4])
    return(course_list)