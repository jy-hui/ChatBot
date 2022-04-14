import random
import json

# read file
sales_json = open('salesInfo.json', 'r')
sales_data = sales_json.read()
sales = json.loads(sales_data)

name = " Jason"
GREET_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey",)
num = range(1, 10)
NUMBER_INPUTS = num

isM1 = False
isM2 = False
isM3 = False

# M2 part
sorry = "Sorry, currently only sell gaming\n" \
        "            related Chair, Table, LED Light and\n" \
        "            Computer Accessories\n\n"
error = "I'm not understand what you mean,\n" \
        "            please tell me again?\n\n"
serve = "We will serve you based on your\n" \
        "            requirement\n\n"
noStock = "Apology to our dear customers,\n" \
          "            currently Computer Accessories\n" \
          "            are no stock.\n" \
          "            Sorry for inconvenience!\n\n"

# rate = 0
# pcs = 1

resp = {

    "hello": [
        "hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me."
    ],

    "what's your name?": [
        "They call me {0}".format(name),
        "My name is the {0}".format(name)],

    "how are you?": [
        "I am feeling good. How about you?",
        "Not so bad. How about you?"],

    "m1": [
        "Welcome to Product Module \n" + "            Any question for you? \n"

    ],
    "m2": [
        "Welcome to Sales Module \n"
        "            What products you prefer to buy? \n"
        "            **Each person able buy max 10 products\n"
        "            (Enter back to quit)\n"
        "            A.Chair \n"
        "            B.Table \n"
        "            C.Computer accessories\n"

    ],
    "m3": [
        "Welcome to Customer Service Module ~\n" + \
        "            Any question for you? \n" + \
        "         -> Refund \n" + \
        "         -> Corporate S3GF \n" + \
        "         -> Contact Us \n" + \
        "         -> More...\n" + \
        "         ** Type 'back' to return to Home Page"

    ],
    "back": ["Welcome back to the S3GF Shop's Home Page, \n" \
             "            I am the S3GF's Chatbot, Jason \n" \
             "            Please choose one of the module task:\n" \
             "            ~ Furniture Product Module \n-> Press 'm1'\n" \
             "            ~ Sales Module \n-> Press 'm2'\n" \
             "            ~ Customer Service Module \n-> Press 'm3'\n"],
    "default": ["This is a default message!"]
}

respM1 = {
    "product": [
        "product", ]
}
respM2 = {
    "sales": ["sales"],
    "a": ["Total amount of chair to buy is?\n"
          "            (Enter z + number)\n"],
    "b": ["Total amount of table to buy is?\n"
          "            (Enter y + number)\n"],
    "s2": ["{0}".format(noStock)],
    "s3": ["{0}".format(serve)],
    "s4": ["{0}".format(sorry)],
    "z1": ["Total 1 of Chair is RM 120"],
    "z2": ["Total 2 of Chairs are RM 240"],
    "z3": ["Total 3 of Chairs are RM 360"],
    "z4": ["Total 4 of Chairs are RM 480"],
    "z5": ["Total 5 of Chairs are RM 600"],
    "z6": ["Total 6 of Chairs are RM 720"],
    "z7": ["Total 7 of Chairs are RM 840"],
    "z8": ["Total 8 of Chairs are RM 960"],
    "z9": ["Total 9 of Chairs are RM 1080"],
    "z10": ["Total 10 of Chairs are RM 1200"],
    "y1": ["Total 1 of Table is RM 200"],
    "y2": ["Total 2 of Tables are RM 400"],
    "y3": ["Total 3 of Tables are RM 600"],
    "y4": ["Total 4 of Tables are RM 800"],
    "y5": ["Total 5 of Tables are RM 1000"],
    "y6": ["Total 6 of Tables are RM 1200"],
    "y7": ["Total 7 of Tables are RM 1400"],
    "y8": ["Total 8 of Tables are RM 1600"],
    "y9": ["Total 9 of Tables are RM 1800"],
    "y10": ["Total 10 of Tables are RM 2000"],
    "default": ["{0}".format(error)]
}

respM3 = {
    "how soon will i receive my refund?": [
        "How soon will I receive my refund?\n" + \
        "           Refunds will be done via the initial payment mode and may take up to 15 working days. Please note that refund amount is subjected to conditions of the products.\n",
    ],
    "how to contact to company?": [
        "Contact Us at 012-12345678 for assistance. \n" + \
        "           Email us at Smart3Gamers@gmail.com\n" + \
        "           For more information : https://serious3gamers.wixsite.com/home\n",
    ]
}


def passData(r, ps, p):
    rateP = r
    psnameP = "ps"
    pcsP = p
    nameS = sales["chairS", "name"]
    value = pcsP * rateP
    price = "Total {0} of ".format(pcsP) + "{0} is RM ".format(psnameP) + "{0}".format(value)
    return price


def res(message):
    global isM1
    global isM2
    global isM3

    if isM1:
        if message in respM1:
            bot_message = random.choice(respM1[message])
        elif message == "back":
            isM1 = False
            isM2 = False
            isM3 = False
            bot_message = random.choice(resp[message])
        else:
            print(message)
            bot_message = random.choice(resp["default"])

    elif isM2:
        if message in respM2:
            bot_message = random.choice(respM2[message])
            print("respM2> {0}".format(message))
        elif message == "back":
            isM1 = False
            isM2 = False
            isM3 = False
            bot_message = random.choice(resp[message])
        else:
            print(message)
            bot_message = random.choice(resp["default"])

    elif isM3:
        if message in respM3:
            bot_message = random.choice(respM3[message])
        elif message == "back":
            isM1 = False
            isM2 = False
            isM3 = False
            bot_message = random.choice(resp[message])
        else:
            print(message)
            bot_message = random.choice(resp["default"])

    else:
        if message in resp:
            print(message)
            if message == "m1":
                isM1 = True
                isM2 = False
                isM3 = False
            elif message == "m2":
                isM1 = False
                isM2 = True
                isM3 = False
            elif message == "m3":
                isM1 = False
                isM2 = False
                isM3 = True
            elif message == "back":
                isM1 = False
                isM2 = False
                isM3 = False
            bot_message = random.choice(resp[message])
        else:
            print(message)
            bot_message = random.choice(resp["default"])
    return bot_message


def real(xtext):
    if xtext in GREET_INPUTS:
        ytext = "hello"
    elif "name" in xtext:
        ytext = "what's your name?"
    elif "contact" in xtext:
        ytext = "how to contact to company?"
    elif "how are" in xtext:
        ytext = "how are you?"
    elif "refund" in xtext:
        ytext = "how soon will i receive my refund?"
    elif "a" in xtext:
        ytext = "a"
        print("a in xtext")
    elif "b" in xtext:
        ytext = "b"
        print("b in xtext")
    elif "c" in xtext:
        ytext = "s2"
        print("c = s2")
    elif "other" in xtext:
        ytext = "s4"
    elif "how many" in xtext:
        ytext = "s3"
    elif "m2" in xtext:
        ytext = "m2"
    else:
        ytext = xtext
    return ytext


def send_message(message):
    # print((message)) # if want block the ytext
    print(message)
    response = res(message)
    return response


# Sales module related function
"""
if my_input.lower() == "a":
    ps = "Chair"
    r = 10
    if my_input.lower() == p:
        pcs = my_input.lower()
        pcs = pcs.int()
        value = pcs * rate
        price = "Total {0} of ".format(pcs) + "{0} is RM ".format(psname) + "{0}".format(value)
        chatWindow.insert(INSERT, "BOT JASON : " + price)
        print("checkB")
        AI.passData(r, ps, pcs)
elif my_input.lower() == "b":
    ps = "Table"
    r = 20
    if my_input.lower() == p:
        pcs = my_input.lower()
        pcs = pcs.int()
        value = pcs * rate
        price = "Total {0} of ".format(pcs) + "{0} is RM ".format(psname) + "{0}".format(value)
        chatWindow.insert(INSERT,
                          "BOT JASON : " + "Total {0} of ".format(pcs) + "{0} is RM ".format(psname) + "{0}".format(
                              value))
        AI.passData(r, ps, pcs)

def check(text):
    if text == "s1":
        send_message(text)
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
                chatWindow.insert(INSERT, "BOT JASON : Continue buying our product(Yes=Y, No=N)> \n")
                next_input = input()
                next_input = next_input.lower()
                checkYes(next_input, finalP)
                break
    elif name == "exit" or name == "stop":
        send_message("6")
    else:
        send_message(text)
        title()
"""
