import string
namesfile = open("names.txt")
namesstring = namesfile.read()
nameslist = namesstring.split(",")
for i in range(len(nameslist)):
    nameslist[i] = nameslist[i].split("\"")[1].lower()
nameslist.sort()
namescoresum = 0
for i in range(len(nameslist)):
    charlist = list(nameslist[i])
    namesubscore = 0
    for j in range(len(charlist)):
        namesubscore += ord(charlist[j]) - ord('a') + 1
    namescoresum += namesubscore * (i + 1)
print namescoresum
