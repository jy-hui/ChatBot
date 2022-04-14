
import webbrowser
import random

from tkinter import *
from tkinter.scrolledtext import ScrolledText

name = " Bot Number 001"
monsoon = "rainy"
mood = "Smiley"

resp = {
    "what's your name?": [
        "They call me {0}".format(name),
        "My name is the {0}".format(name)],

    "what's today's weather?": [
        "The weather is {0}".format(monsoon)],

    "how are you?": [
        "I am feeling {0}".format(mood)],

    "default": ["This is a default message!"]
    }

def res(message):
    if message in resp:
        bot286_message = random.choice(resp[message])
    else:
        bot286_message = random.choice(resp["default"])
    return bot286_message

def real(xtext):
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
    #print((message)) # if want block the ytext
    response = res(message)
    print((response))

root = Tk()

root.title('Chat Bot')
root.configure(bg='Black')
root.geometry('400x500')

main_menu = Menu(root)

file_menu = Menu(root)
file_menu.add_command(label='New..')
file_menu.add_command(label='Save As..')
file_menu.add_command(label='Edit..')

main_menu.add_cascade(label='File', menu=file_menu)
main_menu.add_command(label='Edit')
main_menu.add_command(label='Quit')
root.config(menu=main_menu)

chatWindow = ScrolledText(root, bd=1, bg='white', width=50, height=8)
chatWindow.place(x=5, y=5, height=385, width=385)

messageWindow = Entry(root, bg='white', width=30)
messageWindow.place(x=128, y=400, height=88, width=260)

def send():
    if messageWindow.get():
        my_input = messageWindow.get()
        chatWindow.insert(INSERT, "YOU : " + my_input + "\n")
        messageWindow.delete(0, END)
        # AI THINK
        my_input.lower()
        input1 = real(my_input)
        input2 = send_message(input1)
        if (input2 == "exit" and input2 == "stop"):
            chatWindow.insert(INSERT, "BOT : Thank You very much and Good bye! \n")
            print("End")
        chatWindow.yview_pickplace("end")
    else:
        print("empty")
    print("clicked")

Button = Button(root, text='Send', bg='blue', activebackground='light blue', width=12, height=5, font=('Arial', 20),
                    command=send)
Button.place(x=6, y=400, height=88, width=120)



root.mainloop()

