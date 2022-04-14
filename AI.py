import random

name = " Jason"
GREET_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey",)

isM1 = False
isM2 = False
isM3 = False

# M2 part
sorry = "Sorry, currently only sell gaming related \n     Chair, Table, LED Light and Computer Accessories"
error = "I'm not understand what you mean, please tell me again?"
serve = "We will serve you based on your requirement"
noStock = "Apology to our dear customers, currently Computer Accessories are no stock. \n     Sorry for inconvenience!"
thanks = "Thanks for chatting with me, have a nice day ~ "
amount = "Please enter the amount of this product in number to buy"

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
        "Welcome to Sales Module \n" + \
        "            Any question for you? \n"
        "What products you prefer to buy? (Enter exit to quit)\n"
        "     1.Chair \n     2.Table \n     3.LED Light \n     4.Computer accessories\n"

    ],
    "m3": [
        "Welcome to Customer Service Module \n" + \
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
    "s1": ["Total amount to buy is?"],
    "s2": ["{0}".format(sorry)],
    "s3": ["{0}".format(serve)],
    "s4": ["{0}".format(error)],
    "s5": ["{0}".format(noStock)],
    "s6": ["{0}".format(thanks)],
    "s7": ["{0}".format(amount)],
    "default": ["This is a default message!"]
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
    else:
        ytext = xtext
    return ytext


def productSale(xtext):
    if "chair" in xtext:
        ytext = "s1"
    elif "table" in xtext:
        ytext = "s1"
    elif "led" in xtext:
        ytext = "s1"
    elif "light" in xtext:
        ytext = "s1"
    elif "computer" in xtext:
        ytext = "s5"
    elif "accessories" in xtext:
        ytext = "s5"
    elif "other" in xtext:
        ytext = "s2"
    elif "how many" in xtext:
        ytext = "s3"
    else:
        ytext = "s4"
    return ytext


def send_message(message):
    # print((message)) # if want block the ytext
    print(message)
    response = res(message)
    return response
