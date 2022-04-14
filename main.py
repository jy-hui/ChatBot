import webbrowser
import random
import string

from tkinter import *
from tkinter.scrolledtext import ScrolledText
from PIL import Image, ImageTk

name = "Jason"
isStart = True
isModule3 = False

resp = {
    "what's your name?": [
        "They call me {0}".format(name),
        "My name is the {0}".format(name)],

    #"what's today's weather?": [
    #    "The weather is {0}".format(monsoon)],

    "default": ["This is a default message!"]
    }

def res(message):
    if message in resp:
        bot286_message = random.choice(resp[message])
    else:
        bot286_message = random.choice(resp["default"])
    return bot286_message

def real(xtext): #recorrect the user question
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
    return response

def start():
    text = "BOT JASON : Welcome to the S3GF Shop, \n" \
           "            I am the S3GF's Chatbot, Jason \n" \
           "            Please choose one of the module task:\n" \
           "            ~ Furniture Product Module -> Press 'm1'\n" \
           "            ~ Take Order Module -> Press 'm2'\n" \
           "            ~ Customer Service Module -> Press 'm3'\n"

    return text

def customservice():
    text =''
    return text




root = Tk()

root.title('Smart 3 Gamers Furniture - Chatbot')
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

label1 = Label(root, text = "BOT JASON",bd=1, width=50, height=8,bg='black', fg='white', pady=10, padx=10, font=10)
label1.place(x=5, y=5, height=25, width=385)

chatWindow = ScrolledText(root, bd=1, bg='white', width=50, height=8)
chatWindow.place(x=5, y=35, height=355, width=385)

messageWindow = Entry(root, bg='white', font = (20))
messageWindow.place(x=5, y=400, height=40, width=350)

def send():

    if messageWindow.get():
        my_input = messageWindow.get()
        chatWindow.insert(INSERT, "YOU       : " + my_input + "\n")
        messageWindow.delete(0, END)
        # AI THINK
        if (my_input.lower()=="m1"):
            isModule1 = True
            isStart = False
        elif (my_input.lower()=="m2"):
                isModule2 = True
                isStart = False
        elif (my_input.lower()=="m3"):
            isModule3 = True
            isStart = False
        else:
            chatWindow.insert(INSERT, "BOT JASON : "+ send_message(real(my_input.lower())) +"\n")
            chatWindow.yview_pickplace("end")

    else:
        print("empty")
    print("clicked")

Button = Button(root, text='Send', bg='blue', activebackground='light blue', width=12, height=5, font=('Arial', 20),
                    command=send)
Button.place(x=220, y=450, height=40, width=120)

image1 = PhotoImage(file='S3G.png')

label2 = Label(root,image = image1,bg='black')
label2.place(x=340,y=400)

if(isStart):
    chatWindow.insert(INSERT, start() + "\n")


if(isModule3):
    chatWindow.insert(INSERT, "BOT JASON : " + customservice() + "\n")

root.mainloop()