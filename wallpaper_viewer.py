from tkinter import *
from PIL import ImageTk, Image
import os


def rotate_img():
    global counter
    img_label.config(image=img_list[counter % len(img_list)])
    counter+=1


counter = 1
root = Tk()
root.title("Wallpaper viewer")
root.geometry('250x500')
root.configure(background="black")
files = os.listdir('wallpaper')
img_list = []
for file in files:
    img = Image.open(os.path.join('wallpaper', file))
    resize_img = img.resize((200, 300))
    img_list.append(ImageTk.PhotoImage(resize_img))

img_label = Label(root, image=img_list[0])
img_label.pack(pady=(15, 10))
next_btn = Button(root, text='Next', bg='white', fg='black', width=20, height=2, command=rotate_img)
next_btn.pack()
root.mainloop()
