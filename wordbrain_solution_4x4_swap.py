import json
from wordbrain_good_code import *
import string
import time
import codecs   # For UTF-8 imports
wordlist = loadWords()



inputDict = {}
input4x4 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

while(1):
    input_str = input('Skriv inn dine bokstaver, skilt av mellomrom:' + '\n')
    start_time = time.time()
    input_str = [x.strip() for x in input_str.split(' ')]       # Strip and divide by , and put in a list
    i=0
    for char in input_str:
        inputDict.update({input4x4[i]: char}) 
        i+=1

    input_int = input('Skriv inn lengde på ord, skilt av mellomrom:' + '\n')
    input_int = [x.strip() for x in input_int.split(' ')]       # Strip and divide by , and put in a list
    i=0
    for number in input_int:
        tempDict = {}
        file = open('possibleFourDictLen' + str(number) +'.txt', 'r')
        tempDict = json.load(file)
        file.close()

        tempText =''
        swappedWords = {}
        for item in tempDict:
            for char in item:
                tempText += ''.join(inputDict[char])    # Swap letters in all possible solutions
            swappedWords.update({tempText:tempText})
            tempText = ''
        possibleWords = list(set(swappedWords).intersection(set(wordlist)))  # Get all words found, that exist in the dictionary
        print('Possible ' + str(number) + ' letter words:'  + '\n')
        print(str(sorted(possibleWords))  + '\n')

    end_time = time.time() - start_time
    print('Time used to find solution: ' + str(end_time) + '\n')

