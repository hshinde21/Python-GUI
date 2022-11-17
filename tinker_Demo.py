from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


def valid_login():
    email = email_input.get()
    password = password_input.get()
    if email == 'himanshu@gmail.com' and password == "1234":
        messagebox.showinfo('Yay', 'login successful')
    else:
        messagebox.showerror('Error', "Login Failed")


"""Creating the object of the main class Tk present in the tkinker"""
root = Tk()

"""Changing the title of the UI/tinker screen"""
root.title("Login Screen")

"""Inserting the logo along the title"""
root.iconbitmap("favicon.ico")

"""Controlling the size of the window"""
root.maxsize(400, 400)

"""Creating specific size window"""
root.geometry("350x500")

"""Creating background color"""
root.configure(background='#0096DC')

img = Image.open("flipkart-logo.png")
resized_img = img.resize((70, 70))

"""Opening the filpkart image"""
img = ImageTk.PhotoImage(resized_img)

"""creating a label to print on the screen"""
img_label = Label(root, image=img)

"""Using geometry manager, it decides where to place the UI element """
img_label.pack()

"""Using pady method to move the logo by 10pixel"""
img_label.pack(pady=(10, 10))

"""Setting up the label for the """
text_label = Label(root, text="Flipkart", fg="white", bg='#0096DC', )
text_label.pack()
text_label.config(font=('verdana', 24))
"""Creating email text"""
email_label = Label(root, text="Enter your email", fg="white", bg='#0096DC')
email_label.pack(pady=(20, 5))
email_label.config(font=('verdana', 12))

"""Creating input box for email using Entry class"""
email_input = Entry(root, width=30)
"""using ipady to increase the height"""
email_input.pack(ipady=2, pady=(1, 15))

"""Creating passwrd label"""

password_label = Label(root, text="Enter your password", fg="white", bg='#0096DC')
password_label.pack(pady=(20, 5))
password_label.config(font=('verdana', 12))

"""Creating input box for email using Entry class"""
password_input = Entry(root, width=30)
"""using ipady to increase the height"""
password_input.pack(ipady=2, pady=(1, 15))

"""Creating Login button using button class"""
login_button = Button(root, text="Login", bg="red", fg="black", width=20, heigh=2, command=valid_login)
login_button.pack(pady=(8, 15))
login_button.config(font=('arial', 8))

"""main loop keeps the gui on the screen"""
root.mainloop()
