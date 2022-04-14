import random

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