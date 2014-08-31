import pandas as pd
import numpy as nd

list1 = []
sentimentlist=[]
count = 0
score = []
dictionary = {}
train_data = pd.read_table("train.tsv")
test_data = pd.read_table("test.tsv")

for i in train_data['Phrase']:
    #print dictionary
    list1 = (i.split())
    for word in list1:

        if word in dictionary:
            score = dictionary[word]

            score[0] = ((score[0]*score[1])+train_data['Sentiment'][count])/(score[1]+1.0)
            score[1] = score[1]+1
            dictionary[word] = [score[0],score[1]]
        else:
            score = [train_data['Sentiment'][count],1]
            dictionary[word] = score

    count = count + 1

for j in test_data['Phrase']:
    list1 = j.split()
    tot_sentiment = 0
    count = 0
    for word1 in list1:

        if word1 in dictionary:
            #print word1,"here"
            tot_sentiment = tot_sentiment+dictionary[word1][0]
        else:
            #print word1,"there"
            count = count + 1
    #print list1
    try:
        sentiment = tot_sentiment/(len(list1)-count)
    except:
        sentiment = 2
    sentimentlist.append(int(round(sentiment)))

print (sentimentlist)


answer = test_data['PhraseId']
answer = pd.DataFrame(answer)
answer['Sentiment'] = pd.Series(sentimentlist,index = answer.index)
print answer['Sentiment']
header = ['PhraseId','Sentiment']
answer.to_csv("Submission.csv", index=False)







