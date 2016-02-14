import json
from wordbrain_good_code import *
import string
import time
import codecs   # For UTF-8 imports
#wordlist = loadWords()
wordDict = {}
tempWord = ''
wordDictStart3 = {}

file = open('wordDict-2-9.txt', 'r', encoding='utf-8-sig')
wordlist = json.load(file)
file.close()

for words in wordlist:
    if len(words) > 2:
        for i in range(0,3):
            tempWord += ''.join(words[i])
        wordDictStart3.update({tempWord:tempWord})
        tempWord = ''
#    print(words)

f = open('wordDictStart3.txt','w', encoding='utf-8-sig')
json.dump(wordDictStart3, f)
f.close()

file = open('wordDictStart3.txt', 'r', encoding='utf-8-sig')
wordDictStart3 = json.load(file)
file.close()
