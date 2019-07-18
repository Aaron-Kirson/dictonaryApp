import json
from difflib import get_close_matches

data = json.load(open("data.json", "r"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]

    elif len(get_close_matches(w,data.keys())) > 0:
        yn =  input("did you mean %s instead? type y if yes or n if no: " %  get_close_matches(w, data.keys())[0])

    if yn == "y":
        return get_close_matches(w, data.keys())[0]

    else:
        return "no word found. please double check it"



word = input("please enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)


while True:
    restart = input("Would you like to restart this program? type y if yes or n if no ")

    if restart == "yes" or restart == "y":
        word = input("please enter word: ")
        output = translate(word)

    if restart == "n" or restart == "no":
             print ("program terminating. Goodbye.")
             break
