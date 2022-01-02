import csv

def rearrange(line_len, ori_text):
    new_text = []
    for i in range(len(ori_text)//line_len + 1):
        if i == len(ori_text)//line_len + 1:
            new_text.append(ori_text[(line_len * i)::])
        else:
            new_text.append(ori_text[(line_len * i):(line_len * (i+1))])
    return "\n".join(new_text)


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


def get_course_type_dic(course_list):
    course_dic = {}
    for course in course_list:
        course_dic[course[0]] = f"{course[1]}課"
    return course_dic

def read_event(event_type, name):
    f = open(f"text/event/{event_type}/{name}.txt", mode = "r", encoding = "utf-8-sig")
    text = f.readlines()
    seperated_text = []
    for line in text:
        if line != "\n":
            line = line.strip()
        seperated_text.append(line)

    f.close()
    return seperated_text