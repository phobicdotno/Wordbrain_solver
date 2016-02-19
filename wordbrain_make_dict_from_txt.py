import json
from wordbrain_good_code import *
import string
import time
import codecs   # For UTF-8 imports
#wordlist = loadWords()
wordDict = {}
tempWord = ''
wordDictStart9 = {}

file = open('wordDict-2-9.txt', 'r', encoding='utf-8-sig')
wordlist = json.load(file)
file.close()

for words in wordlist:
    if len(words) > 8:
        for i in range(0,9):
            tempWord += ''.join(words[i])
        wordDictStart9.update({tempWord:tempWord})
        tempWord = ''
#    print(words)

f = open('wordDictStart9.txt','w', encoding='utf-8-sig')
json.dump(wordDictStart9, f)
f.close()

file = open('wordDictStart9.txt', 'r', encoding='utf-8-sig')
wordDictStart9 = json.load(file)
file.close()
