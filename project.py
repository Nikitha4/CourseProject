# Author: Moksh Shah

import json
from collections import defaultdict
from collections import Counter


def rankings(searchengineresult):

    names = []

    for x in searchengineresult:
        names.append(x[0])

    counts = Counter(names)

    return dict(sorted(counts.items(), key=lambda item: item[1]))



def searchengine(wordstomes, query) :

    querywords = query.split()

    newq = querywords[0]

    messages = wordstomes[newq]

    finalmessages = []
    for x in messages:
        if query in x[1]:
            finalmessages.append(x)

    return finalmessages



def main() :

    print("Program Running. Press Ctrl+C to Exit")
    jsonfilename = input("Enter JSON File Name: ")

    with open(jsonfilename, "r") as read_file:
        data = json.load(read_file)

    participants = []
    for i in range(len(data["participants"])):
        participants.append(data["participants"][i]["name"])

    messages = []
    for i in range(len(data["messages"])):
        messages.append((data["messages"][i]["sender_name"], data["messages"][i]["content"]))

    words_to_messages = defaultdict(list)

    for i in range((len(messages))):
        mescontent = messages[i][1]
        contentwords = mescontent.split()
        for j in range(len(contentwords)):
            words_to_messages[contentwords[j]].append(messages[i])
            
    while (True):
    
        query = input("Query: ")
        searched_messages = searchengine(words_to_messages, query)

        for i in range(len(searched_messages)):
            print("Result #: " + str(i + 1) + ", Name: " + searched_messages[i][0] + ", Content: " + searched_messages[i][1])   

        f = rankings(searched_messages)

        print(f)



def exitmain() :
    try :
        main()

    except KeyboardInterrupt:
        print("\nExiting Program")

    except FileNotFoundError:
        print("File Not Found\n")
        exitmain()


exitmain()
