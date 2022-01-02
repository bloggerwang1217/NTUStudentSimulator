import tkinter as tk
from tkinter import font 
from PIL import ImageTk, Image
import function.status as status
import function.sound_effect as sound
import system.semester as semester
import random

warning = "警示用全域變數"

def course_selection(window, data):

    widgets = []
    used_widgets = []

    f = tk.font.Font(size = 24)
    list_f = tk.font.Font(size = 16)

    ntu_course_selection = Image.open("figure/ntu_course_selection.png")
    ntu_course_selection = ImageTk.PhotoImage(ntu_course_selection)
    title = tk.Label(window, image = ntu_course_selection)
    title.image = ntu_course_selection
    title.pack()
    widgets.append(title)

    ntu_course_bottom = Image.open("figure/ntu_course_bottom.png")
    ntu_course_bottom = ImageTk.PhotoImage(ntu_course_bottom)
    bottom = tk.Label(window, image = ntu_course_bottom)
    bottom.image = ntu_course_bottom
    bottom.pack(side = "bottom")
    widgets.append(bottom)

    background = tk.Canvas(window, bg="#c5d2f1", height = 180, width = 1280 * 0.9, bd = 5, relief = "raised")
    text = background.create_text(20, 20, text = "課程類別選擇", font = f, anchor=tk.NW)
    course1 = background.create_text(1 * background.winfo_reqwidth()/4, 50, text = "課程1", font = list_f, anchor=tk.NW)
    course2 = background.create_text(2 * background.winfo_reqwidth()/4, 50, text = "課程2", font = list_f, anchor=tk.NW)
    course3 = background.create_text(3 * background.winfo_reqwidth()/4, 50, text = "課程3", font = list_f, anchor=tk.NW)
    canvas_clear = [course1, course2, course3]

    background.place(x = 640-background.winfo_reqwidth()/2, y = 3 * title.winfo_reqheight()/2)
    widgets.append(background)

    # 讀取目前課程狀態
    course_option = {"涼課":[], "爽課":[], "硬課":[], "甜課":[]}
    course_type_option = []
    
    for item in data["status"].course:
        if item[1] == "涼" and item[2]-item[3] > 0:
            course_option["涼課"].append(item[0])
        elif item[1] == "廢" and item[2]-item[3] > 0:
            course_option["爽課"].append(item[0])
        elif item[1] == "硬" and item[2]-item[3] > 0:
            course_option["硬課"].append(item[0])
        elif item[1] == "甜" and item[2]-item[3] > 0:
            course_option["甜課"].append(item[0])

    line = ""
    for course_type in course_option.keys():
        if len(course_option[course_type]) == 0:
            if line == "":
                line += f"{course_type}"
            else:
                line += f"、{course_type}"
        else:
            course_type_option.append(course_type)


    if line != "":
        announcement = tk.Label(window, text = f"{line}被你修完啦！", font = f)
        announcement.place(x = 640 - announcement.winfo_reqwidth()/2, y = 1.6 * background.winfo_reqheight())
        used_widgets.append(announcement)

    picked_type = [tk.StringVar(), tk.StringVar(), tk.StringVar()]
    for i in range(len(picked_type)):
        picked_type[i].set(course_type_option[0])

    course1List = tk.OptionMenu(window, picked_type[0], *course_type_option)
    course2List = tk.OptionMenu(window, picked_type[1], *course_type_option)
    course3List = tk.OptionMenu(window, picked_type[2], *course_type_option)
    course1List.config(bg = "#c5d2f1")
    course2List.config(bg = "#c5d2f1")
    course3List.config(bg = "#c5d2f1")

    course1List.place(x = 640-background.winfo_reqwidth()/2 + 1 * background.winfo_reqwidth()/4 - 5, y = 3 * title.winfo_reqheight()/2 + 100)
    course2List.place(x = 640-background.winfo_reqwidth()/2 + 2 * background.winfo_reqwidth()/4 - 5, y = 3 * title.winfo_reqheight()/2 + 100)
    course3List.place(x = 640-background.winfo_reqwidth()/2 + 3 * background.winfo_reqwidth()/4 - 5, y = 3 * title.winfo_reqheight()/2 + 100)
    used_widgets.append(course1List)
    used_widgets.append(course2List)
    used_widgets.append(course3List)

    printButton = tk.Button(window, text = "確認", font = f, command = lambda: [display_course_type(window, data, printButton, background, used_widgets, widgets, canvas_clear, picked_type, course_option), sound.play_button_sound()])
    printButton.place(x = 640 + background.winfo_reqwidth()/2 - 2 * printButton.winfo_reqwidth(), y = background.winfo_reqheight() + printButton.winfo_reqheight())
    used_widgets.append(printButton)


def display_course_type(window, data, printButton, background, used_widgets, widgets, text, picked_type, course_option):
    f = tk.font.Font(size = 24)
    button_f = tk.font.Font(size = 36)

    for i in [0, 1, 2]:
        picked_type[i] = picked_type[i].get()
        background.delete(text[i])

    course1 = background.create_text(1 * background.winfo_reqwidth()/4, 50, text = picked_type[0], font = f, anchor=tk.NW)
    course2 = background.create_text(2 * background.winfo_reqwidth()/4, 50, text = picked_type[1], font = f, anchor=tk.NW)
    course3 = background.create_text(3 * background.winfo_reqwidth()/4, 50, text = picked_type[2], font = f, anchor=tk.NW)
    
    for widget in used_widgets:
        widget.destroy()

    picked_course = [tk.StringVar(), tk.StringVar(), tk.StringVar()]
    for i in range(len(picked_type)):
        picked_course[i].set(course_option[picked_type[i]][0])

    course1List = tk.OptionMenu(window, picked_course[0], *course_option[picked_type[0]])
    course2List = tk.OptionMenu(window, picked_course[1], *course_option[picked_type[1]])
    course3List = tk.OptionMenu(window, picked_course[2], *course_option[picked_type[2]])
    course1List.config(bg = "#c5d2f1")
    course2List.config(bg = "#c5d2f1")
    course3List.config(bg = "#c5d2f1")

    course1List.place(x = 640-background.winfo_reqwidth()/2 + 1 * background.winfo_reqwidth()/4, y = 3 * widgets[0].winfo_reqheight()/2 + 100)
    course2List.place(x = 640-background.winfo_reqwidth()/2 + 2 * background.winfo_reqwidth()/4, y = 3 * widgets[0].winfo_reqheight()/2 + 100)
    course3List.place(x = 640-background.winfo_reqwidth()/2 + 3 * background.winfo_reqwidth()/4, y = 3 * widgets[0].winfo_reqheight()/2 + 100)
    widgets.append(course1List)
    widgets.append(course2List)
    widgets.append(course3List)

    printButton = tk.Button(window, text = "顯示選課結果", font = button_f, command = lambda: [display_course(window, data, widgets, picked_course), sound.play_button_sound()])
    printButton.place(x = 640 - printButton.winfo_reqwidth()/2, y = 720 - 3 * printButton.winfo_reqheight())
    widgets.append(printButton)


def display_course(window, data, used_widgets, picked_course_from_menu):
    f = tk.font.Font(size = 24)
    button_f = tk.font.Font(size = 36)
    title_f = tk.font.Font(size = 48)

    picked_course = []

    for i in [0, 1, 2]:
        picked_course.append(picked_course_from_menu[i].get())
    
    if picked_course[0] == picked_course[1] or picked_course[1] == picked_course[2] or picked_course[0] == picked_course[2]:
        global warning
        warning = tk.Label(window, text = "請勿選相同的課", fg = "#712322", font = title_f)
        warning.place(x = 640 - warning.winfo_reqwidth()/2, y = 360 - warning.winfo_reqheight()/2)
        return

    widgets = []

    time = {'1-1': '週一早上', '1-2': '週一下午', '1-3': '週一晚上', '2-1': '週二早上', '2-2': '週二中午', '2-3': '週二晚上', '3-1': '週三早上', '3-2': '週三下午', '3-3': '週三晚上', '4-1': '週四早上', '4-2': '週四下午', '4-3': '週四晚上', '5-1': '週五早上', '5-2': '週五下午', '5-3': '週五晚上'}
    picked_time = random.sample(time.keys(), 3)

    for widget in used_widgets:
        widget.destroy()

    ntu_course_result = Image.open("figure/ntu_course_result.png")
    ntu_course_result = ImageTk.PhotoImage(ntu_course_result)
    title = tk.Label(window, image = ntu_course_result)
    title.image = ntu_course_result
    title.pack()
    widgets.append(title)

    text_title = tk.Label(window, text = "選課結果", fg = "#712322", font = title_f)
    text_title.place(x = 640 - text_title.winfo_reqwidth()/2, y = title.winfo_reqheight())
    widgets.append(text_title)

    course1 = tk.Label(window, text = f"1.{picked_course[0]}, 時間:{time[picked_time[0]]}\n", font = f)
    course2 = tk.Label(window, text = f"2.{picked_course[1]}, 時間:{time[picked_time[1]]}\n", font = f)
    course3 = tk.Label(window, text = f"3.{picked_course[2]}, 時間:{time[picked_time[2]]}\n", font = f)
    course1.place(x = 640 - 3 * text_title.winfo_reqwidth()/4, y = title.winfo_reqheight()+course1.winfo_reqheight()*2)
    course2.place(x = 640 - 3 * text_title.winfo_reqwidth()/4, y = title.winfo_reqheight()+course2.winfo_reqheight()*4)
    course3.place(x = 640 - 3 * text_title.winfo_reqwidth()/4, y = title.winfo_reqheight()+course3.winfo_reqheight()*6)    
    widgets.append(course1)
    widgets.append(course2)
    widgets.append(course3)

    picked = {}
    for i in range(3):
        picked[picked_time[i]] = picked_course[i]

    start_semester = tk.Button(window, text = "繼續", font = button_f, command = lambda: [press_start_semester(window, data, widgets, picked), sound.play_button_sound()])
    start_semester.place(x = 640 - start_semester.winfo_reqwidth()/2, y = 720 - 2 * start_semester.winfo_reqheight())
    widgets.append(start_semester)

    try:
        warning.destroy()
    except:
        pass

def press_start_semester(window, data, widgets, picked):
    for widget in widgets:
        widget.destroy()
    data["picked_course"] = picked

    semester.start_semester(window, data, picked, "大一上")