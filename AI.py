import random
import json

# read file
product_json = open('furniture_data.json', 'r')
product_data = product_json.read()
product = json.loads(product_data)
product_chair = product['chair']
product_table = product['table']
product_accessories = product['accessories']

faq_json = open('FAQ.json', 'r')
faq_data = faq_json.read()
faq = json.loads(faq_data)
faq_question = faq['FAQ']

name = " Jason"
GREET_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey",)

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
        "         ** Type 'back' to return to Home Page\n\n"],
    "m2": [
        "Welcome to Sales Module \n"
        "            What products you prefer to buy? \n"
        "            **Each person able buy max 10 products\n"
        "            (Enter alphabet twice, Eg. aa)\n"
        "            A.Chair \n"
        "            B.Table \n"
        "            C.Computer accessories\n"
        "         ** Type 'back' to return to Home Page\n\n"],
    "m3": [
        "Welcome to Customer Service Module ~\n" + \
        "            Any question for you? \n" + \
        "         -> Refund \n" + \
        "         -> Corporate S3GF \n" + \
        "         -> Contact Us \n" + \
        "         -> More...\n" + \
        "         ** Type 'back' to return to Home Page\n\n"
    ],
    "back": ["Welcome back to the S3GF's Home Page,\n" \
             "            I am the S3GF's Chatbot, Jason \n" \
             "            Please choose one of the module task:\n" \
             "            ~ Furniture Product Module \n"
             "                  -> Press 'm1'\n" \
             "            ~ Sales Module \n"
             "                  -> Press 'm2'\n" \
             "            ~ Customer Service Module \n"
             "                  -> Press 'm3'\n"],
    "default": ["{0}".format(error)]
}

respM1 = {
    "chair": [
        "This is all of our chair product,\n" +
        "            can ask any of this product\n" +
        "            -> " + product_chair[0].get("name") + "\n" +
        "            -> " + product_chair[1].get("name") + "\n" +
        "            -> " + product_chair[2].get("name") + "\n" +
        "            -> " + product_chair[3].get("name") + "\n" +
        "            -> " + product_chair[4].get("name") + "\n"],
    "table": [
        "This is all of our table product,\n" +
        "            can ask any of this product\n" +
        "            -> " + product_table[0].get("name") + "\n" +
        "            -> " + product_table[1].get("name") + "\n" +
        "            -> " + product_table[2].get("name") + "\n" +
        "            -> " + product_table[3].get("name") + "\n" +
        "            -> " + product_table[4].get("name") + "\n"],
    "accessories": [
        "This is all of our accessories product,\n" +
        "            can ask any of this product\n" +
        "            -> " + product_accessories[0].get("name") + "\n" +
        "            -> " + product_accessories[1].get("name") + "\n" +
        "            -> " + product_accessories[2].get("name") + "\n" +
        "            -> " + product_accessories[3].get("name") + "\n" +
        "            -> " + product_accessories[4].get("name") + "\n" +
        "            -> " + product_accessories[5].get("name") + "\n" +
        "            -> " + product_accessories[6].get("name") + "\n"
    ],
    "TTRacing Maxx Gaming Chair": [
        "Name: " + product_chair[0].get("name") + "\n" +
        "            Price: " + product_chair[0].get("price") + "\n" +
        "            Color: " + product_chair[0].get("color") + "\n" +
        "            Height: " + product_chair[0].get("height") + "\n" +
        "            Description: \n" + product_chair[0].get("description") + "\n"
    ],
    "TTRacing Maxx Air Threads Fabric Gaming Chair": [
        "Name: " + product_chair[1].get("name") + "\n" +
        "            Price: " + product_chair[1].get("price") + "\n" +
        "            Color: " + product_chair[1].get("color") + "\n" +
        "            Height: " + product_chair[1].get("height") + "\n" +
        "            Description: \n" + product_chair[1].get("description") + "\n"
    ],
    "TTRacing Duo V3 Gaming Chair": [
        "Name: " + product_chair[2].get("name") + "\n" +
        "            Price: " + product_chair[2].get("price") + "\n" +
        "            Color: " + product_chair[2].get("color") + "\n" +
        "            Height: " + product_chair[2].get("height") + "\n" +
        "            Description: \n" + product_chair[2].get("description") + "\n"
    ],
    "TTRacing Swift X 2020 Gaming Chair": [
        "Name: " + product_chair[3].get("name") + "\n" +
        "            Price: " + product_chair[3].get("price") + "\n" +
        "            Color: " + product_chair[3].get("color") + "\n" +
        "            Height: " + product_chair[3].get("height") + "\n" +
        "            Description: \n" + product_chair[3].get("description") + "\n"
    ],
    "Vertagear  PL6000": [
        "Name: " + product_chair[4].get("name") + "\n" +
        "            Price: " + product_chair[4].get("price") + "\n" +
        "            Color: " + product_chair[4].get("color") + "\n" +
        "            Height: " + product_chair[4].get("height") + "\n" +
        "            Description: \n" + product_chair[4].get("description") + "\n"
    ],
    "L Shape Gaming Table": [
        "Name: " + product_table[0].get("name") + "\n" +
        "            Price: " + product_table[0].get("price") + "\n" +
        "            Color: " + product_table[0].get("color") + "\n" +
        "            Size: " + product_table[0].get("size") + "\n" +
        "            Description: \n" + product_table[0].get("description") + "\n"
    ],
    "GTGAMEZ Z Series Gaming Table": [
        "Name: " + product_table[1].get("name") + "\n" +
        "            Price: " + product_table[1].get("price") + "\n" +
        "            Color: " + product_table[1].get("color") + "\n" +
        "            Size: " + product_table[1].get("size") + "\n" +
        "            Description: \n" + product_table[1].get("description") + "\n"
    ],
    "GT-Ultra Lite Height Adjustable Gaming Desk": [
        "Name: " + product_table[2].get("name") + "\n" +
        "            Price: " + product_table[2].get("price") + "\n" +
        "            Color: " + product_table[2].get("color") + "\n" +
        "            Size: " + product_table[2].get("size") + "\n" +
        "            Description: \n" + product_table[2].get("description") + "\n"
    ],
    "NILOR-K Type Gaming Table": [
        "Name: " + product_table[3].get("name") + "\n" +
        "            Price: " + product_table[3].get("price") + "\n" +
        "            Color: " + product_table[3].get("color") + "\n" +
        "            Size: " + product_table[3].get("size") + "\n" +
        "            Description: \n" + product_table[3].get("description") + "\n"
    ],
    "R5 Premium LED Gaming Table": [
        "Name: " + product_table[4].get("name") + "\n" +
        "            Price: " + product_table[4].get("price") + "\n" +
        "            Color: " + product_table[4].get("color") + "\n" +
        "            Size: " + product_table[4].get("size") + "\n" +
        "            Description: \n" + product_table[4].get("description") + "\n"
    ],
    "Neck Pillow": [
        "Name: " + product_accessories[0].get("name") + "\n" +
        "            Price: " + product_accessories[0].get("price") + "\n" +
        "            Color: " + product_accessories[0].get("color") + "\n"
    ],
    "Lumbar Pillow": [
        "Name: " + product_accessories[1].get("name") + "\n" +
        "            Price: " + product_accessories[1].get("price") + "\n" +
        "            Color: " + product_accessories[1].get("color") + "\n"
    ],
    "Desk Pad": [
        "Name: " + product_accessories[2].get("name") + "\n" +
        "            Price: " + product_accessories[2].get("price") + "\n" +
        "            Color: " + product_accessories[2].get("color") + "\n"
    ],
    "Chair Mat": [
        "Name: " + product_accessories[3].get("name") + "\n" +
        "            Price: " + product_accessories[3].get("price") + "\n" +
        "            Color: " + product_accessories[3].get("color") + "\n"
    ],
    "Multi-purpose Leather Cleaner": [
        "Name: " + product_accessories[4].get("name") + "\n" +
        "            Price: " + product_accessories[4].get("price") + "\n" +
        "            Color: " + product_accessories[4].get("color") + "\n" +
        "            Description :\n" +
        "Is a spray cleaner that can clean your chair and table"
    ],
    "Tomaz Gaming Floorpad": [
        "Name: " + product_accessories[5].get("name") + "\n" +
        "            Price: " + product_accessories[5].get("price") + "\n" +
        "            Color: " + product_accessories[5].get("color") + "\n"
    ],
    "LED Strip light": [
        "Name: " + product_accessories[6].get("name") + "\n" +
        "            Price: " + product_accessories[6].get("price") + "\n" +
        "            Color: " + product_accessories[6].get("color") + "\n"
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
respM2 = {
    "sales": ["sales"],
    "aa": ["This is all of our chair product,\n" +
           "            -> " + product_chair[0].get("name") + "\n" +
           "            -> " + product_chair[1].get("name") + "\n" +
           "            -> " + product_chair[2].get("name") + "\n" +
           "            -> " + product_chair[3].get("name") + "\n" +
           "            -> " + product_chair[4].get("name") + "\n" +
           "Total amount of chair to buy is?\n"
           "            (Enter z + number)\n"],
    "bb": ["This is all of our table product,\n" +
           "            -> " + product_table[0].get("name") + "\n" +
           "            -> " + product_table[1].get("name") + "\n" +
           "            -> " + product_table[2].get("name") + "\n" +
           "            -> " + product_table[3].get("name") + "\n" +
           "            -> " + product_table[4].get("name") + "\n" +
           "Total amount of table to buy is?\n"
           "            (Enter y + number)\n"],
    "s2": ["{0}".format(noStock) +
           "This is all of our accessories product,\n" +
           "            -> " + product_accessories[0].get("name") + "\n" +
           "            -> " + product_accessories[1].get("name") + "\n" +
           "            -> " + product_accessories[2].get("name") + "\n" +
           "            -> " + product_accessories[3].get("name") + "\n" +
           "            -> " + product_accessories[4].get("name") + "\n" +
           "            -> " + product_accessories[5].get("name") + "\n" +
           "            -> " + product_accessories[6].get("name") + "\n" +
           "            Please come to our retails shop!\n"],
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
        "\n\tFAQ : "+faq_question[0].get("question")+"\n\tANS : "+faq_question[0].get("answer"),
    ],
    "how to contact to company?": [
        "\n\tFAQ : "+faq_question[1].get("question")+"\n\tANS : "+faq_question[1].get("answer"),
    ],
    "what should i do if my item is damaged?": [
        "\n\tFAQ : "+faq_question[2].get("question")+"\n\tANS : "+faq_question[2].get("answer"),
    ],
    "are chemicals used in the manufacturing process of s3gf products?": [
        "\n\tFAQ : "+faq_question[3].get("question")+"\n\tANS : "+faq_question[3].get("answer"),
    ],
    "do your products contain lead?": [
        "\n\tFAQ : "+faq_question[4].get("question")+"\n\tANS : "+faq_question[4].get("answer"),
    ],
    "do you recycle products?": [
        "\n\tFAQ : "+faq_question[5].get("question")+"\n\tANS : "+faq_question[5].get("answer"),
    ],
    "who owns the s3gf concept?": [
        "\n\tFAQ : "+faq_question[6].get("question")+"\n\tANS : "+faq_question[6].get("answer"),
    ],
    "where is s3gf store?": [
        "\n\tFAQ : "+faq_question[7].get("question")+"\n\tANS : "+faq_question[7].get("answer"),
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
    elif "damaged" in xtext:
        ytext = "what should i do if my item is damaged?"
    elif "chemical" in xtext:
        ytext = "are chemicals used in the manufacturing process of s3gf products?"
    elif "lead" in xtext:
        ytext = "do your products contain lead?"
    elif "recycle" in xtext:
        ytext = "do you recycle products?"
    elif "corporate" in xtext:
        ytext = "who owns the s3gf concept?"
    elif "where" in xtext:
        ytext = "where is s3gf store?"
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
    elif "chair" in xtext:
        ytext = "chair"
    elif "table" in xtext:
        ytext = "table"
    elif "accessories" in xtext:
        ytext = "accessories"
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
    elif "aa" in xtext:
        ytext = "aa"
        print("a in xtext")
    elif "bb" in xtext:
        ytext = "bb"
        print("b in xtext")
    elif "cc" in xtext:
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
