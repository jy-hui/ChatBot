import random

name = " Jason"
GREET_INPUTS = ("hello","hi","greetings","sup","what's up","hey",)


isM1 = False
isM2 = False
isM3 = False

resp = {

    "hello":[
        "hi","hey","*nods*", "hi there","hello","I am glad! You are talking to me."
    ],

    "what's your name?": [
        "They call me {0}".format(name),
        "My name is the {0}".format(name)],

    "how are you?": [
        "I am feeling good. How about you?",
        "Not so bad. How about you?"],

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
        "         -> Refund \n" +\
        "         -> Corporate S3GF \n" +\
        "         -> Contact Us \n" +\
        "         -> More...\n"+\
        "         ** Type 'back' to return to Home Page"



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
    "product": [
        "product",]
}
respM2 = {
    "order": [
        "order",]
}
respM3 = {
    "refund":[
        " ",
    ],
    "how to contact to company?":[
        "Contact Us at 012-12345678 for assistance. \n" +\
        "           Email us at Smart3Gamers@gmail.com" +\
        "           For more information : https://serious3gamers.wixsite.com/home",
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
    else:
        ytext = xtext
    return ytext

def send_message(message):
    #print((message)) # if want block the ytext
    print(message)
    response = res(message)
    return response

