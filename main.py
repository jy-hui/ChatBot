from tkinter import *

root = Tk()

root.title('Chat Bot')
root.frame()
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

chatWindow = Text(root, bd=1, bg='black', width=50, height=8)
chatWindow.place(x=6, y=6, height=385, width=370)

messageWindow = Text(root, bg='black', width=30, height=4)
messageWindow.place(x=128, y=400, height=88, width=260)

Button = Button(root, text='Send', bg='blue', activebackground='light blue', width=12, height=5, font=('Arial', 20))
Button.place(x=6, y=400, height=88, width=120)

scrollbar = Scrollbar(root, command=chatWindow.yview())
scrollbar.place(x=375, y=5, height=385)

root.mainloop()