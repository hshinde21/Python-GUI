import io
import webbrowser

import requests
import json
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk, Image


class News_App:
    def __init__(self):
        self.data = requests.get(
            'https://newsapi.org/v2/top-headlines?country=us&apiKey=620fcdeb28e441d18838c879b7a2bc1c').json()

        self.load_gui()

        self.load_news_item(0)

    def load_gui(self):
        self.root = Tk()
        self.root.geometry('350x600')
        self.root.resizable(0, 0)
        self.root.title("news app")
        self.root.configure(background='purple')

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def load_news_item(self, index):
        self.clear()
        try:
            img_url = self.data['articles'][index]['urlToImage']
            raw_data = urlopen(img_url).read()
            imgg = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(imgg)
            label = Label(self.root, image=photo)
            label.pack()
        except:
            img_url = 'https://www.hhireb.com/wp-content/uploads/2019/08/default-no-img.jpg'
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)

        label = Label(self.root,image=photo)
        label.pack()

        heading = Label(self.root, text=self.data['articles'][index]['title'], bg='black', fg='white', wraplength=350,
                        justify='center')
        heading.pack(pady=(10, 20))
        heading.config(font=('verdana', 15))

        details = Label(self.root, text=self.data['articles'][index]['description'], bg='black', fg='white',
                        wraplength=350,
                        justify='center')
        details.pack(pady=(2, 20))
        details.config(font=('verdana', 12))

        """To place the button we have to use Frame"""
        frame = Frame(self.root)
        frame.pack(expand=True, fill=BOTH)
        if index != 0:
            previous_btn = Button(frame, text='prev', width=16, height=3, command=self.load_news_item(index - 1))
            previous_btn.pack(side=LEFT)

        readmore_btn = Button(frame, text='Read More', width=16, height=3,
                              command=lambda: self.open_link(self.data['articles'][index]['url']))
        readmore_btn.pack(side=LEFT)

        if index != len(self.data['articles']) - 1:
            Next_btn = Button(frame, text='Next', width=16, height=3, command=self.load_news_item(index + 1))
            Next_btn.pack(side=LEFT)

        self.root.mainloop()

    def open_link(self, url):
        webbrowser.open(url)


obj = News_App()
