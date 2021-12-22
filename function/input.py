import tkinter as tk


def input_basic_data():
    # Top level window
    frame = tk.Tk()
    frame.title("姓名、性別輸入（無法顯示注音，但仍可方向鍵選字）")
    frame.geometry('400x200')

    data = ["", ""]
    # TextBox Creation
    inputtxt = tk.Text(frame,
                       height = 5,
                       width = 20)

    inputtxt.config(highlightthickness=2, highlightbackground="black")
    inputtxt.pack()

    var1 = tk.IntVar()
    var2 = tk.IntVar()
    c1 = tk.Checkbutton(frame, text="男性",variable=var1, onvalue=1, offvalue=0)
    c1.pack()
    c2 = tk.Checkbutton(frame, text='女性',variable=var2, onvalue=1, offvalue=0)
    c2.pack()

    # Label Creation
    lbl = tk.Label(frame)
    lbl.pack()

    # Button Creation
    endButton = tk.Button(frame,
            text = "結束", 
            command = lambda :end_input(frame))

    printButton = tk.Button(frame,
                            text = "確認", 
                            command = lambda: save_input(data, var1, var2, inputtxt, lbl, frame, endButton))
    printButton.pack()


      
    frame.mainloop()

    return data


def save_input(data, var1, var2, inputtxt, lbl, frame, endButton):
    sex = ""
    if var1.get() + var2.get() == 1:        
        if (var1.get() == 1) and (var2.get() == 0):
            sex = "男性"
        elif (var1.get() == 0) & (var2.get() == 1):
            sex =  "女性"
        inp = inputtxt.get(1.0, "end-1c")
        lbl.config(text = f"您的名字是「{inp}」，{sex}，不想重新輸入請按結束")
        endButton.pack()
    else:
        inp = inputtxt.get(1.0, "end-1c")
        lbl.config(text = f"您的名字是「{inp}」，請苟選一個最認同的性別")
        endButton.pack_forget()
    data[1] = sex
    data[0] = inp


def end_input(frame):
    frame.destroy()

