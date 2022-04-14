import random
from tkinter import INSERT

from main import chatWindow

sorry = "Sorry, currently only sell gaming related \n     Chair, Table, LED Light and Computer Accessories"
error = "I'm not understand what you mean, please tell me again?"
serve = "We will serve you based on your requirement"
noStock = "Apology to our dear customers, currently Computer Accessories are no stock. \n     Sorry for inconvenience!"
thanks = "Thanks for chatting with me, have a nice day ~ "
amount = "Please enter the amount of this product in number to buy"

resp = {
    "1": ["BOT: Total amount to buy is?"],
    "2": ["BOT: {0}".format(sorry)],
    "3": ["BOT: {0}".format(serve)],
    "4": ["BOT: {0}".format(error)],
    "5": ["BOT: {0}".format(noStock)],
    "6": ["BOT: {0}".format(thanks)],
    "7": ["BOT: {0}".format(amount)],
    "default": ["This is a default message!"]
}


def res(message):
    if message in resp:
        bot286_message = random.choice(resp[message])
    else:
        bot286_message = random.choice(resp["default"])
    return bot286_message


def productIs(xtext):
    if "chair" in xtext:
        ytext = "1"
    elif "table" in xtext:
        ytext = "1"
    elif "led" in xtext:
        ytext = "1"
    elif "light" in xtext:
        ytext = "1"
    elif "computer" in xtext:
        ytext = "5"
    elif "accessories" in xtext:
        ytext = "5"
    elif "other" in xtext:
        ytext = "2"
    elif "how many" in xtext:
        ytext = "3"
    else:
        ytext = "4"
    return ytext


# Used or inside if statement will error

def send_message(message):
    # print((message)) # if want block the ytext
    response = res(message)
    print(response)


def title():
    print("\nBOT: What products you prefer to buy? (Enter exit to quit)")
    print("     1.Chair \n     2.Table \n     3.LED Light \n     4.Computer accessories")
    print("")
    my_input = input()
    my_input = my_input.lower()
    related_text = productIs(my_input)
    check(related_text, my_input)


def totalNumber(name, num):
    if name == "chair":
        price = 20
    elif name == "table":
        price = 50
    elif name == "led":
        price = 15
    elif name == "light":
        price = 15
    else:
        price = 0
    totalP = num * price
    print("BOT: Total {0} of ".format(num) + "{0} is RM ".format(name) + "{0}".format(totalP))
    return totalP


def checkYes(i, finalP):
    if i == "y":
        finalP += finalP
        title()
    else:
        print("Total Price of all products are RM{0}".format(finalP))
        send_message("6")
        quit()


def check(text, name):
    if text == "1":
        send_message(text)
        num_input = input()
        for m in num_input:
            if not m.isdigit():
                send_message("7")
                check("1", name)
                break
            else:
                num_input = int(num_input)
                totalP = totalNumber(name, num_input)
                finalP = totalP
                print("Continue buying our product(Yes=Y, No=N)> ")
                next_input = input()
                next_input = next_input.lower()
                checkYes(next_input, finalP)
                break
    elif name == "exit" or name == "stop":
        send_message("6")
    else:
        send_message(text)
        title()


def sale():
    while 1:
        print("BOT: Hello dear customer, Our S3GF provide gaming related furnitures")
        title()
        print("BOT: Enter exit to quit, thanks ~")
        my_input = input()
        my_input = my_input.lower()
        if my_input == "exit" or my_input == "stop":
            break
