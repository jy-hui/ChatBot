import webbrowser
from tkinter import *
from tkinter.scrolledtext import ScrolledText

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
        chatWindow.insert(INSERT,"YOU : "+messageWindow.get()+"\n")
        messageWindow.delete(0, END)

        chatWindow.yview_pickplace("end")
    else:
        print("empty")
    print("clicked")

Button = Button(root, text='Send', bg='blue', activebackground='light blue', width=12, height=5, font=('Arial', 20), command=send)
Button.place(x=6, y=400, height=88, width=120)



root.mainloop()