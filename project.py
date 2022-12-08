import json
from collections import defaultdict
from collections import Counter



#print(data)



def rankings(searchengineresult):

    names = []

    for x in searchengineresult:
        names.append(x[0])

    
    counts = Counter(names)

    #print(counts)

    #orderedres = []

    

    return dict(sorted(counts.items(), key=lambda item: item[1]))





def searchengine(wordstomes, query) :

    #messages = wordstomes[query]

    querywords = query.split()

    #querymessages = []

    #for x in querywords:
    #    querymessages.append(wordstomes[x])

    
    #for i in range(len(querymessages)):

    newq = querywords[0]

    messages = wordstomes[newq]

    finalmessages = []
    for x in messages:
        if query in x[1]:
            finalmessages.append(x)




    return finalmessages



def main() :
    with open("data.json", "r") as read_file:
        data = json.load(read_file)

    participants = []
    for i in range(len(data["participants"])):
        participants.append(data["participants"][i]["name"])

    #print(participants)
    #print(data["participants"][0]["name"])

    num_participants = len(participants)

    #message[] = (sendername, content)
    messages = []
    for i in range(len(data["messages"])):
        messages.append((data["messages"][i]["sender_name"], data["messages"][i]["content"]))

    #print(messages)

    words_to_messages = defaultdict(list)

    for i in range((len(messages))):
        mescontent = messages[i][1]
        contentwords = mescontent.split()
        #print(contentwords)
        for j in range(len(contentwords)):
            
            words_to_messages[contentwords[j]].append(messages[i])
            #print( words_to_messages[contentwords[j]])
    #print(words_to_messages)

    m = searchengine(words_to_messages, "im ready")
    #print(m)
    #for i in range(len(m)):
        #print("#: " + str(i) + ", Name: " + m[i][0] + ", Content: " + m[i][1])   


    print(m)

    f = rankings(m)

    #print(f)





main()
