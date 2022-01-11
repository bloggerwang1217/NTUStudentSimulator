import system.beginning as bg
import tkinter as tk
import os

window = tk.Tk()
window.geometry("1280x720")
window.resizable(0, 0)
window.title("為美好的台大生活獻上祝福")

data = {}
bg.start_game(window, data)

window.mainloop()
path = os.getcwd()
try:
    for name in data["ability_graph"]:
        os.remove(f"{path}/figure/ability/{name}.png")
    os.remove(f"{path}/figure/ability/finalpix.png")
except:
    pass