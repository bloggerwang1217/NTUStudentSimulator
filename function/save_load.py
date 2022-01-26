import function.status as status
import function.read_file as read
import system.semester as semester
from pathlib import Path
from os import fspath
import os


def clear(graph_list):
    path = os.getcwd()
    for entry in os.listdir(f"{path}/figure/ability"):
        if entry[0:-4] not in graph_list and entry[0] != ".":
            os.remove(fspath(Path(f"{path}/figure/ability/{entry[0:-4]}.png")))


def save(data):
    data["status"].yang_sheng = int(data["status"].yang_sheng)
    sex = data["sex"]
    name = data["name"]
    CsCs = data["色色"]
    status = data["status"]
    time = data["time"]
    ability_graph = data["ability_graph"]
    freq = list(status.freq)

    f1 = open(fspath(Path("text/save.csv")), "w")
    str_course = []
    for i in range(len(status.course)):
        str_course.append([])
        str_course[i] = status.course[i].copy()
        str_course[i][2] = str(status.course[i][2])
        str_course[i][3] = str(status.course[i][3])
        str_course[i][4] = str(status.course[i][4])

    for course in str_course:
        f1.write(",".join(course)+"\n")
    
    f1.close()

    f2 = open(fspath(Path("text/save.txt")), "w")

    if CsCs == True:
        CsCs = "True"
    else:
        CsCs = "False"

    f2.write(sex+","+name+","+CsCs+","+time+"\n")
    f2.write(f"{status.wisdom},{status.charm},{status.fitness},{status.social},{status.health},{status.luck},{status.love_progress},{status.grade},{status.yang_sheng},{status.prestige},{status.money},{status.time}\n")
    f2.write(f"{status.achievement.number_of_sex},{status.achievement.being_Vtuber},{status.achievement.stocks_surfing},{status.achievement.christmas},{status.achievement.birth}\n")
    f2.write(",".join(ability_graph)+"\n")

    for i in range(len(freq)):
        if freq[i] == True:
            freq[i] = "True"
        else:
            freq[i] = "False"

    f2.write(",".join(freq))
    
    f2.close()

    f3 = open(fspath(Path("text/picked.txt")), "w")

    f3.write(",".join(list(data["picked_course"].keys()))+"\n")
    f3.write(",".join(list(data["picked_course"].values())))

    f3.close()

    clear(data["ability_graph"])  # 刪除名稱沒有在save.txt的圖片


def load(window, data):
    f1 = open(fspath(Path("text/save.txt")), "r")
    read_data = f1.readlines()
    for i in range(len(read_data)):
        read_data[i] = read_data[i].strip("\n").split(",")
    data["sex"], data["name"], data["色色"], data["time"] = read_data[0][0], read_data[0][1], read_data[0][2], read_data[0][3]

    if data["色色"] == "True":
        data["色色"] = True
    else:
        data["色色"] = False

    for i in range(len(read_data[1])):
        read_data[1][i] = int(read_data[1][i])

    data["status"] = status.Status(read_data[1][0], read_data[1][1], read_data[1][2], read_data[1][3], read_data[1][4], read_data[1][5], read.read_course(Path("text/save.csv")), window)
    data["status"].love_progress = read_data[1][6]
    data["status"].grade = read_data[1][7]
    data["status"].yang_sheng = read_data[1][8]
    data["status"].prestige = read_data[1][9]
    data["status"].money = read_data[1][10]
    data["status"].time = read_data[1][11]
    data["ability_graph"] = read_data[3]

    for i in range(len(read_data[4])):
        if read_data[4][i] == "True":
            read_data[4][i] = True
        else:
            read_data[4][i] = False

    data["status"].freq = tuple(read_data[4])

    data["status"].achievement.number_of_sex = int(read_data[2][0])
    data["status"].achievement.stocks_surfing = int(read_data[2][2])
    if read_data[2][1] == "False":
        data["status"].achievement.being_Vtuber = False
    else:
        data["status"].achievement.being_Vtuber = True

    if read_data[2][3] == "False":
        data["status"].achievement.christmas = False
    else:
        data["status"].achievement.christmas = True

    if read_data[2][4] == "False":
        data["status"].achievement.birth = False
    else:
        data["status"].achievement.birth = True

    f1.close()

    f2 = open(fspath(Path("text/picked.txt")), "r")
    picked_list = f2.readlines()
    picked_list[0] = picked_list[0].strip("\n").split(",")
    picked_list[1] = picked_list[1].split(",")
    picked_dict = {}
    for i in range(len(picked_list[0])):
        picked_dict[picked_list[0][i]] = picked_list[1][i]
    data["picked_course"] = picked_dict

    f2.close()

    semester.start_semester(window, data, picked_dict, data["time"])
'''
sex
name
色色
status
time
ability_graph

Status
status.wisdom int  
status.charm int  
status.fitness int  
status.social int  
status.health int 
status.money int  
status.luck int  
status.love_progress int  
status.grade int  
status.yang_sheng int  
status.prestige int 
status.course list  
status.achievement = achievement.Achievement()
status.time int
status.freq = True, True, True, True, True, True, True, True, True, True (tuple)

Achievement
self.number_of_sex = 0
self.being_Vtuber = False
self.stocks_surfing = 0
self.christmas = False
self.birth = False
'''