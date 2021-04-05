from SpotipyMethods import SpotipyMethods
import time
from owScore import OwScore
from threading import Thread
from tkinter import Label, Tk, Button
import threading
import urllib

if __name__ == "__main__":
    import os
    owScore = OwScore()
    window = Tk()


    window.title("OW record")
    window.geometry('600x600')

    ow_score_string = owScore.get_test_string()
    lbl_score = Label(window, text=ow_score_string, font=("Arial Bold", 30))
    lbl_score.grid(column=0, row=0)


    btnWinPlus = Button(window, text="Wins +", font=("Arial Bold", 30), command= lambda: owScore.winsPlus(lbl_score), bg="#000080",fg="white",)
    btnWinLess = Button(window, text="Wins -", font=("Arial Bold", 30),  command= lambda: owScore.winsLess(lbl_score), bg="#000080",fg="white",)
    btnLoosePlus = Button(window, text="Loose +", font=("Arial Bold", 25), command= lambda: owScore.loosesPlus(lbl_score), bg="#000080",fg="white",)
    btnLooseLess = Button(window, text="Loose -", font=("Arial Bold", 25), command= lambda: owScore.loosesLess(lbl_score), bg="#000080",fg="white",)
    btnDrawPlus = Button(window, text="Draw +", font=("Arial Bold", 30), command= lambda: owScore.drawPlus(lbl_score), bg="#000080",fg="white",)
    btnDrawLess = Button(window, text="Draw -", font=("Arial Bold", 30), command= lambda: owScore.drawLess(lbl_score), bg="#000080",fg="white",)
    btnReset = Button(window, text="Reset", font=("Arial Bold", 30), command= lambda: owScore.reset(lbl_score), bg="#000080",fg="white",)

    btnWinPlus.grid(column=0, row=1)
    btnWinLess.grid(column=1, row=1)
    btnReset.grid(column=2, row=1)
    btnLoosePlus.grid(column=0, row=2)
    btnLooseLess.grid(column=1, row=2)
    btnDrawLess.grid(column=1, row=3)
    btnDrawPlus.grid(column=0, row=3)

    spotipyString = SpotipyMethods.get_current_song()

    # Spotipy
    lbl = Label(window, text=spotipyString, font=("Arial Bold", 15), justify='left', anchor='w')
    lbl.grid(column=0, row=5, columnspan=3)

    def change_label():
        t1 = threading.Thread(target=SpotipyMethods.change_label_of_song, args=(lbl,))
        t1.setDaemon(True)
        t1.start()

    def refresh_label():
        lbl.configure(text=SpotipyMethods.get_current_song())
        SpotipyMethods.change_label_of_song_txt(lbl.cget("text"))

    change_label_song = Button(window, text="Refresh", font=("Arial Bold", 30), command=refresh_label, bg="#000080",fg="white",)
    change_label_song.grid(column=1, row=4)

    window.after(1000,change_label)
    window.mainloop()

    # To make an exe use:
    # pyinstaller file_name.py
    # Inside the program directory in this case:
    #   cd C:\Users\Edu\Documents\VisualStudio\CODES\PYTHON\spotipy
    #   pyinstaller main.py


