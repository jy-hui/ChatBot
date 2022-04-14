import webbrowser
import random
import string
import nltk
import sys
import os

from tkinter import *
from tkinter.scrolledtext import ScrolledText
from PIL import Image, ImageTk

import AI
import salesProduct

name = "Jason"
isStart = True
isModule3 = False

resp = {
    "what's your name?": [
        "They call me {0}".format(name),
        "My name is the {0}".format(name)],
    "default": ["This is a default message!"]
}


def res(message):
    if message in resp:
        bot286_message = random.choice(resp[message])
    else:
        bot286_message = random.choice(resp["default"])
    return bot286_message


def real(xtext):  # recorrect the user question
    if "name" in xtext:
        ytext = "what's your name?"
    elif "weather" in xtext:
        ytext = "what's today's weather?"
    elif "how are" in xtext:
        ytext = "how are you?"
    else:
        ytext = ""
    return ytext


def send_message(message):
    # print((message)) # if want block the ytext
    response = res(message)
    print(response)
    return response


def start():
    text = "BOT JASON : Welcome to the S3GF Shop, \n" \
           "            I am the S3GF's Chatbot, Jason \n" \
           "            Please choose one of the module task:\n" \
           "            ~ Furniture Product Module -> Press 'm1'\n" \
           "            ~ Take Order Module -> Press 'm2'\n" \
           "            ~ Customer Service Module -> Press 'm3'\n"

    return text


root = Tk()

root.title('Smart 3 Gamers Furniture - Chatbot')
root.configure(bg='Black')
root.geometry('450x500')


def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, *sys.argv)


main_menu = Menu(root)

file_menu = Menu(root, tearoff=False)
file_menu.add_command(label='Restart', command=restart_program)
file_menu.add_command(label='Quit', command=root.destroy)

main_menu.add_cascade(label='More', menu=file_menu)

root.config(menu=main_menu)

label1 = Label(root, text="BOT JASON", bd=1, width=50, height=8, bg='black', fg='white', pady=10, padx=10, font=10)
label1.place(x=5, y=5, height=25, width=440)

chatWindow = ScrolledText(root, bd=1, bg='white', width=50, height=8)
chatWindow.place(x=5, y=35, height=355, width=440)
chatWindow.insert(INSERT, start() + "\n")

messageWindow = Entry(root, bg='white', font=(20))
messageWindow.place(x=5, y=400, height=40, width=375)


def send():
    if messageWindow.get():
        my_input = messageWindow.get()
        chatWindow.insert(INSERT, "YOU       : " + my_input + "\n")
        messageWindow.delete(0, END)
        # AI THINK
        chatWindow.insert(INSERT, "BOT JASON : " + AI.send_message(AI.real(my_input.lower())) + "\n")
        chatWindow.yview_pickplace("end")

    else:
        print("empty")
    print("clicked")


Button = Button(root, text='Send', bg='blue', activebackground='light blue', width=12, height=5, font=('Arial', 20),
                command=send)
Button.place(x=260, y=450, height=40, width=120)

image1 = PhotoImage(file='S3G.png')

label2 = Label(root, image=image1, bg='black')
label2.place(x=390, y=400)

root.mainloop()
