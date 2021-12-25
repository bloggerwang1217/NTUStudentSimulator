def read_beginning():
    f = open("text/beginning.txt", mode = "r", encoding = "utf-8")
    text = f.readlines()
    f.close()
    return text