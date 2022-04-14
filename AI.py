import random

name = " Jason"

isM1 = False
isM2 = False
isM3 = False

resp = {
    "what's your name?": [
        "They call me {0}".format(name),
        "My name is the {0}".format(name)],

    "m1":[
        "Welcome to Product Module \n" + "            Any question for you? \n"

    ],
    "m2": [
        "Welcome to Order Module \n" +\
        "            Any question for you? \n"

    ],
    "m3": [
        "Welcome to Customer Service Module \n" +\
        "            Any question for you? \n" + \
        "         1. Return and refund online order \n" +\
        "         2. Corporate S3GF \n" +\
        "         3. Contact Us \n"


    ],
    "back": ["Welcome back to the S3GF Shop's Home Page, \n" \
           "            I am the S3GF's Chatbot, Jason \n" \
           "            Please choose one of the module task:\n" \
           "            ~ Furniture Product Module -> Press 'm1'\n" \
           "            ~ Take Order Module -> Press 'm2'\n" \
           "            ~ Customer Service Module -> Press 'm3'\n"],
    "default": ["This is a default message!"]
    }

respM1 = {
    "Product": [
        "product",]
}
respM2 = {
    "Order": [
        "order",]
}
respM3 = {
    "Help":[
        "help me",
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
    if "name" in xtext:
        ytext = "what's your name?"
    elif "weather" in xtext:
        ytext = "what's today's weather?"
    elif "how are" in xtext:
        ytext = "how are you?"
    else:
        ytext = xtext
    return ytext

def send_message(message):
    #print((message)) # if want block the ytext
    print(message)
    response = res(message)
    return response

