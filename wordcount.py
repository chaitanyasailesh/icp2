file = open("sample.txt","r")
wordcount = {}
for word in file.read().split():
    if word.lower() in wordcount:
        wordcount[word.lower()] += 1
    else:
        wordcount[word.lower()] = 1
for k, v in wordcount.items():
    print(k, v )