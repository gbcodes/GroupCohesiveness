from tkinter import *
from facial_analysis import process_all_images, show_webcam, show_video
from tkinter import filedialog


root = Tk()
root.geometry('1260x800')
root.resizable(width=False, height=False)

title = Label(root, text='Group Cohesion')

title['font'] = 'Montserrat 26 bold'
title.pack(fill=X)

def image_clicked():
    global filename
    filename = filedialog.askopenfilename()
    process_all_images(filename)

def video_clicked():
    global video
    video = filedialog.askopenfilename()
    show_video(video)

def camera_clicked():
    show_webcam()

post_title = Label(root, text='Система определения групповой сплоченности')
post_title["fg"] = "#1E90FF"
post_title["font"] = 'Montserrat 17 bold'
post_title.pack(fill=X)

question = Label(root, text='Пожалуйста, выберите что вы хотите сделать')
question["font"] = "Montserrat 20"
question.pack(fill=X)

button1 = Button(root, text='Загрузить изображение', width=25, height=2, bg='white', fg='black', font='Montserrat 16',
                 command=image_clicked)
button1.place(x=20, y=550)

button2 = Button(root, text='Загрузить видео', width=25, height=2, bg='white', fg='black', font='Montserrat 16',
                 command=video_clicked)
button2.place(x=470, y=550)

button3 = Button(root, text='Включить камеру', width=25, height=2, bg='white', fg='black', font='Montserrat 16',
                 command=show_webcam)
button3.place(x=920, y=550)

user = Label(root, font='Montserrat 16')
user.place(x=680, y=200)
person = Label(root, font='Montserrat 16')

from PIL import Image, ImageTk

img = ImageTk.PhotoImage(Image.open("img.png"))
panel = Label(root, image = img)
panel.place(x=205, y=120)
root.mainloop()
print(filename)

