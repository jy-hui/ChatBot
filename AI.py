import random

name = " Jason"
GREET_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey",)

isM1 = False
isM2 = False
isM3 = False

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
        "Welcome to Product Module \n" +
        "            What kind of product you want to ask?\n" +
        "            -> Chair\n" +
        "            -> Table\n" +
        "            -> Accessories\n" +
        "         ** Type 'back' to return to Home Page"],
    "m2": [
        "Welcome to Sales Module \n" + \
        "            Any question for you? \n"

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
    "chair": [
        "This is all of our chair product,\n" +
        "            can ask any of this product\n" +
        "            -> TTRacing Maxx\n" +
        "            -> TTRacing Maxx Air Threads Fabric\n" +
        "            -> TTRacing Duo V3\n" +
        "            -> TTRacing Swift X 2020\n" +
        "            -> Vertagear  PL6000\n"],
    "table":[
        "This is all of our table product,\n" +
        "            can ask any of this product\n" +
        "            -> L Shape Gaming Table\n" +
        "            -> GTGAMEZ Z Series Gaming Table\n" +
        "            -> GT-Ultra Lite Height Adjustable Gaming Desk\n" +
        "            -> NILOR-K Type Gaming Table\n" +
        "            -> R5 Premium LED Gaming Table\n"],
    "accessories": [
        "This is all of our accessories product,\n" +
        "            can ask any of this product\n" +
        "            -> Neck Pillow\n" +
        "            -> Lumbar Pillow\n" +
        "            -> Desk Pad\n" +
        "            -> Chair Mat\n" +
        "            -> Multi-purpose Leather Cleaner\n" +
        "            -> Tomaz Gaming Floorpad\n" +
        "            -> LED Strip light\n"],
    "TTRacing Maxx": [
        "Name: TTRacing Maxx Gaming Chair\n" +
        "            Price: RM 1099\n" +
        "            Color:  Black\n" +
        "            Height: 140-160cm\n" +
        "            Description :\n" +
        "The proud result of countless hours of designing and decisions made, the whole new Maxx Series Gaming Chair "
        "shall be exalted, providing the utmost comfort with its wide and tall body and seat. Refined craftsmanship "
        "culminating the ideal dressing for Maxx Series Gaming Chair.\n "
    ],
    "TTRacing Maxx Air Threads Fabric Gaming Chair": [
        "Name: TTRacing Maxx Air Threads Fabric\n" +
        "            Price: RM 1149\n" +
        "            Color:  Black\n" +
        "            Height: 150-170cm\n" +
        "            Description :\n"+
        "The Maxx Venom’s new fish scales design allows you to bond perfectly with the chair with the right amount of resistance. Become the most dangerous being around with uninterrupted peak level performance. You’ll never want to leave this chair again.\n"
    ],
    "TTRacing Duo V3 Gaming Chair": [
        "Name: TTRacing Duo V3 Gaming Chair\n" +
        "            Price: RM 359\n" +
        "            Color:  Black, Red\n" +
        "            Height: 120-130cm\n" +
        "            Description :\n" +
        "We pride ourselves calling Duo V3 the best entry gaming chair that you will find. The brand new Duo V3 comes with pristine face lift and equipped with top quality parts. With wider and taller body and seat, the Duo V3 is able to cater to most users, providing equal amount of comfort and pleasure sitting on this masterpiece. "
   ],
    "TTRacing Swift X 2020 Gaming Chair": [
        "Name: TTRacing Swift X 2020 Gaming Chair\n" +
        "            Price: RM 599\n" +
        "            Color:  Black, Red\n" +
        "            Height: 150-180cm\n" +
        "            Description :\n" +
        "The champion’s upholstery, the Air Threads fabric is the perfect blend of smoothness, softness and breathability. Created meticulously from the best textile, down to the threads, creating an airy sensation in style. Braided to perfection, the Air Threads is made of crossing threads that deliver the right amount of resistance for uninterrupted top level performance. Maximized for long hours of cooling comfort made exclusively for the strivers."
    ],
    "Vertagear  PL6000": [
        "Name: Vertagear  PL6000\n" +
        "            Price: RM 1799\n" +
        "            Color:  Black, White, Blue\n" +
        "            Height: 150-170cm\n" +
        "            Description :\n" +
        "Industrial strength materials and thoughtful design provide extra room for comfort for those who desire more space or plan to spend extended periods in their gaming sessions."
  ],
    "L Shape Gaming Table": [
        "Name: L Shape Gaming Table\n" +
        "            Price: RM 199\n" +
        "            Color: Black, Red\n" +
        "            Size: 120x45x75cm\n" +
        "            Description :\n" +
        "Powder coat metal steel, melamine table top, waterproof, smooth Surface"
    ],
    "GTGAMEZ Z Series Gaming Table": [
        "Name: GTGAMEZ Z Series Gaming Table\n" +
        "            Price: RM 269\n" +
        "            Color: Black, Red, White\n" +
        "            Size: 120x55x75cm\n" +
        "            Description :\n" +
        " 3D Rounded Edges ; Carbon Fiber Surface ; Strong Structure ; High Load Bearing ; Sturdy Body & Leg Design ; Anti-Slip on the table leg to Prevent Scratched Floor"
   ],
    "GT-Ultra Lite Height Adjustable Gaming Desk": [
        "Name: GT-Ultra Lite Height Adjustable\n" +
        "            Price: RM 699\n" +
        "            Color: Black\n" +
        "            Size: 110x60x118cm\n" +
        "            Description :\n" +
        "Height adjustable (73CM-118CM), Modern look & solid, Strong structure leg, increase stability, Carbon-fiber texture tabletop ,Excellent load bearing, not shaking"
   ],
    "NILOR-K Type Gaming Table": [
        "Name: NILOR-K Type Gaming Table\n" +
        "            Price: RM 189\n" +
        "            Color: Black\n" +
        "            Size: 120x60x75cm\n" +
        "            Description :\n" +
        "This desk for gaming is specially designed for gamers, constructed by durable metal frame legs, this table for gaming not only looks cool and stylish, very solid and stable with no wobble."
  ],
    "R5 Premium LED Gaming Table": [
        "Name: R5 Premium LED Gaming Table\n" +
        "            Price: RM 369 \n" +
        "            Color: Black, Red\n" +
        "            Size: 120x60x72cm\n" +
        "            Description :\n" +
        "This desk for gaming is specially designed for gamers, constructed by durable metal frame legs, this R-line table for gaming not only looks cool and stylish, very solid and stable with no wobble."
    ],
    "Neck Pillow": [
        "Name: Neck Pillow\n" +
        "            Price: RM 50 \n" +
        "            Color: Black, Yellow\n"
    ],
    "Lumbar Pillow": [
        "Name: Lumbar Pillow\n" +
        "            Price: RM 100 \n" +
        "            Color: Black, Yellow\n"
    ],
    "Desk Pad": [
        "Name: Desk Pad\n" +
        "            Price: RM 50 \n" +
        "            Color: Black\n"
    ],
    "Chair Mat": [
        "Name: Chair Mat\n" +
        "            Price: RM 100 \n" +
        "            Color: Black, Yellow\n"
    ],
    "Multi-purpose Leather Cleaner": [
        "Name: Multi-purpose Leather Cleaner\n" +
        "            Price: RM 99\n" +
        "            Color: Black, Yellow\n" +
        "            Description :\n" +
        "Is a spray cleaner that can clean your chair and table"
    ],
    "Tomaz Gaming Floorpad": [
        "Name: Tomaz Gaming Floorpad\n" +
        "            Price: RM 120 \n" +
        "            Color: Black, Red\n"
    ],
    "LED Strip light": [
        "Name: LED Strip light\n" +
        "            Price: RM 10 \n"
    ],
    "i want to order": [
        "If you want order the product, you can back to menu and select Sales Module\n"
    ],
    "is this product good ?": [
        "All of this product are good quality\n"
    ],
    "what is tha warranty of the product": [
        "All of the product in Chair and Table are 2 Years-Warranty\n"
    ],
    "how was the design of the product": [
        "All of the product are nice design\n"
    ],
    "who are suitable for this product": [
        "All of the product are design for gaming purpose\n"
    ],
    "what are this product design for": [
        "All of the product are design for gaming purpose\n"
    ],
    "how should i clean the chair or table": [
        "you can buy Multi-purpose Leather Cleaner to clean your table and chair"
    ],
    "default": ["Sorry, i dont understand",
                "please give related information"]
}
product1 = {
    "1": [
        "1.TTRacing Maxx Gaming Chair\n"
    ]
}

respM2 = {
    "sales": [
        "sales", ]
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
    elif "maxx" in xtext:
        ytext = "TTRacing Maxx Gaming Chair"
    elif "air threads" in xtext:
        ytext = "TTRacing Maxx Air Threads Fabric Gaming Chair"
    elif "duo" in xtext:
        ytext = "TTRacing Duo V3 Gaming Chair"
    elif "swift" in xtext:
        ytext = "TTRacing Swift X 2020 Gaming Chair"
    elif "pl6000" in xtext:
        ytext = "Vertagear  PL6000"
    elif "l shape" in xtext:
        ytext = "L Shape Gaming Table"
    elif "gtgamez" in xtext:
        ytext = "GTGAMEZ Z Series Gaming Table"
    elif "ultra" in xtext:
        ytext = "GT-Ultra Lite Height Adjustable Gaming Desk"
    elif "nilor" in xtext:
        ytext = "NILOR-K Type Gaming Table"
    elif "r5" in xtext:
        ytext = "R5 Premium LED Gaming Table"
    elif "neck" in xtext:
        ytext = "Neck Pillow"
    elif "lumbar" in xtext:
        ytext = "Lumbar Pillow"
    elif "desk" in xtext:
        ytext = "Desk Pad"
    elif "chair mat" in xtext:
        ytext = "Chair Mat"
    elif "cleaner" in xtext:
        ytext = "Multi-purpose Leather Cleaner"
    elif "floorpad" in xtext:
        ytext = "Tomaz Gaming Floorpad"
    elif "led stripe light" in xtext:
        ytext = "LED Strip light"

    elif "order" in xtext:
        ytext = "i want to order"
    elif "good" in xtext:
        ytext = "is this product good ?"
    elif "warranty" in xtext:
        ytext = "what is tha warranty of the product"
    elif "design for" in xtext:
        ytext = "what are this product design for"
    elif "design" in xtext:
        ytext = "how was the design of the product"
    elif "suitable" in xtext:
        ytext = "who are suitable for this product"
    elif "clean" in xtext:
        ytext = "how should i clean the chair or table"
    else:
        ytext = xtext
    return ytext


def send_message(message):
    # print((message)) # if want block the ytext
    print(message)
    response = res(message)
    return response
