import json
from wordbrain_good_code import *
import string
import time
import codecs   # For UTF-8 imports
wordlist = loadWords()
wordDict = {}

for words in wordlist:
    wordDict.update({words:words})
#    print(words)

f = open('wordDict-2-9.txt','w', encoding='utf-8-sig')
json.dump(wordDict, f)
f.close()

file = open('wordDict-2-9.txt', 'r', encoding='utf-8-sig')
tempDict = json.load(file)
file.close()
