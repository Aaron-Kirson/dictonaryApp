import json
from difflib import get_close_matches

data = json.load(open("data.json", "r"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]

    elif len(get_close_matches(w,data.keys())) > 0:
        yn =  input("did you mean %s instead? type y if yes or n if no: " %  get_close_matches(w, data.keys())[0])
    else:
            return "We didn't understand your entry."

    if yn == "y" or yn == "yes":
        return data[get_close_matches(w, data.keys())[0]]

    else:
        return "no word found. please double check it"


def start_app(word):
    output = translate(word)

    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)



word = input("please enter a word to find out the meaning: ")
start_app(word)




while True:
    restart = input("Would you like to restart this program? type y if yes or n if no: ")


    if restart.lower() == "yes" or restart.lower() == "y":
        word = input("please enter a word to find out the meaning: ")
        start_app(word)

    elif restart == "n" or restart == "no":
             print ("program terminating. Goodbye.")
             break
