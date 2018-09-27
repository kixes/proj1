import sys
#set the file to be counted
filename = sys.argv[1]
file=open( filename ,"r+")

#create variables
wordcount={}
extrawords={}
totalwords=0
differentwords=0
#loop through file
for word in file.read().split():
    totalwords=totalwords+1
    word = word.lower()
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

#extract words that have "in" or has greater then 3 chars
wordcount.values().sort()
for key,val in wordcount.items():
    if len( key ) > 3 or 'in' in key :
        differentwords=differentwords+1
        extrawords[key]=val
        wordcount.pop(key, None)

#Print extracted words
for w in sorted(extrawords, key=extrawords.get,reverse=True):
    print w, extrawords[w]

#print all other words
for w in sorted(wordcount, key=wordcount.get,reverse=True):
    print w, wordcount[w]

print "\ntotal words:"
print totalwords
print "\ndifferent words:"
print differentwords
