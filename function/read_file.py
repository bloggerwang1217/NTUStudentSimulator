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


def read_class():
    f = open("text/class.csv", mode = "r", encoding = "utf-8")
    csvReader = csv.reader(f)
    class_dic = {}
    for row in csvReader:
        if row[0] != "課程":
            class_dic[row[0]] = [row[1], int(row[2])]
    return(class_dic)