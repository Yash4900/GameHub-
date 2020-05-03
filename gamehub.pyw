from tkinter import *
from tkinter.ttk import Progressbar
import time
import threading
import random
import os
import pygame
import playsound
pygame.init()

def start_snakes(*args):
	pygame.mixer.music.stop()
	playsound.playsound('sounds/SELECT.mp3')
	root.withdraw()
	os.system('python snakegame.py')
	root.deiconify()
	pygame.mixer.music.play()

def start_flappy(*args):
	pygame.mixer.music.stop()
	playsound.playsound('sounds/SELECT.mp3')
	root.withdraw()
	os.system('python main.py')

	root.deiconify()
	pygame.mixer.music.play()

def start_racing(*args):
	pygame.mixer.music.stop()
	playsound.playsound('sounds/SELECT.mp3')
	root.withdraw()
	os.system('python cargame.py')
	root.deiconify()
	pygame.mixer.music.play()


def pause():
	progress['value'] = 20
	time.sleep(1)
	progress['value'] = 40
	time.sleep(1)
	progress['value'] = 50
	time.sleep(1)
	progress['value'] = 60
	time.sleep(1)
	progress['value'] = 80
	time.sleep(1)
	progress['value'] = 100
	progress.pack_forget()
	title.pack_forget()
	load.pack_forget()
	pygame.mixer.music.play()
	select.pack(anchor=NW)
	l4.pack(side=TOP, anchor=NW)
	l1.pack(padx=45, side=LEFT)
	l1.bind("<Button-1>", start_snakes)
	l2.pack(padx=45, side=LEFT)
	l2.bind("<Button-1>", start_flappy)
	l3.pack(padx=45, side=LEFT)
	l3.bind("<Button-1>", start_racing)


	
root = Tk()
root.configure(bg="black")
root.geometry("800x500")
root.maxsize(800,500)
root.title("Gamehub")
root.wm_iconbitmap('img/game_1.ico')
title = Label(root,text="Welcome To Gamehub",font="consolas 40", fg="white", bg="black")
title.pack(pady=180)
load = Label(root, text="Loading...", font="consolas", fg="white", bg="black")
load.pack(side=TOP)
progress = Progressbar(root,orient=HORIZONTAL,length=500,mode='determinate')
progress.pack()
t1 = threading.Thread(target=pause)
t1.start()
pygame.mixer.music.load('sounds/Bgaudio.mp3')
select = Label(root,text="Select your Game :)",font="consolas 30", fg="white", bg="black")
snake = PhotoImage(file="img/snake.png")
l1 = Label(root, image=snake, borderwidth=0)
flappy = PhotoImage(file="img/flappy.png")
l2 = Label(root, image=flappy, borderwidth=0)
carrace = PhotoImage(file="img/carrace.png")
l3 = Label(root, image=carrace, borderwidth=0)
line = PhotoImage(file="img/Line.png")
l4 = Label(root, image=line, borderwidth=0)
root.mainloop()

