
import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import filedialog, messagebox, Toplevel, Frame, Scrollbar
from tkinter.filedialog import askopenfilename, asksaveasfilename, askdirectory
from tkinter import filedialog

# import tkinter.scrolledtext
from tkinter import scrolledtext as st
from tkinter import *
import tkinter.colorchooser
import os, pathlib
import pyautogui as pg
import pyperclip as pc
import glob
import time





class Ooder(object):
    
    def __init__(self,parent):
        self.parent = parent
        self.top = Toplevel()
        self.frm1 = ttk.Frame(self.parent, width=1200, height=900)
        self.frm1.grid(row=1, column=4)
       
        self.btn1 = tk.Button(self.frm1, text="find x y", bg="orange", bd=6,command=self.print_mouse_position)
        self.btn1.grid(row=5, column=1)
        self.btn2 = tk.Button(self.frm1, text="MOVE1", bg="orange", bd=6,command=self.new_move)
        self.btn2.grid(row=6, column=1)




            

    def print_mouse_position(self):
        while True:
            time.sleep(5)
            x, y = pg.position()
            positionStr = "X: " + str(x).rjust(4) + " Y: " + str(y).rjust(4)
            print(positionStr)

    def new_move(self):
        for i in range(1600, 3480, 50):
            pg.moveTo(i,850,0.25)
            pg.click(i,550)
        for i in range(1600, 3480, 50):
             pg.moveTo(i,950,0.25)
             pg.click(i,650)

        for i in range(1600, 3480, 50):
            pg.moveTo(i,1050,0.25)
            pg.click(i,750)
        for i in range(1600, 3480, 50):
             pg.moveTo(i,850,0.25)
             pg.click(i,850)



##        for j in range(400, 1100, 100):
##            pg.moveTo(2000,j)
##            pg.click(2000,j)
##    
            
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        c = Ooder(self)
        self.geometry('1200x600')
        self.resizable(True, True)

if __name__ == "__main__":
    app=App()
    app.mainloop()

