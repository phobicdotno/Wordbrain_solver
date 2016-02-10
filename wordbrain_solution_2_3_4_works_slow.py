# WORDBRAIN SOLUTION

import string
import time
import codecs   # For UTF-8 imports
import json     # For saving to file
from wordbrain_graphs import *
from wordbrain_good_code import *

# variables
words=''
wordlist = loadWords()

def show2x2pathsPossible(endpoints2x2, twoGraph):
    all_paths = {}
    for item in twoGraph:
	#Result: ['a', 'b', 'c', 'd']
        for i in range(1,len(endpoints2x2[item])):
            # twoGraph[item][0] = key/start node
            # endpoints2x2[item][i] = end node
            all_paths.update(find_all_paths_from_to(twoGraph,
            twoGraph[item][0], endpoints2x2[item][i]))
            #Result: ['bd', 'bcad', 'bcd', 'bacd', 'bad']
    return all_paths

def manualInput2x2(wordlist, ch0, ch1, ch2, ch3):
    twoGraph = make2x2graph(ch0, ch1, ch2, ch3)
    print(twoGraph)
    endpoints2x2 = makeEndPoints2x2(ch0, ch1, ch2, ch3)
    print(endpoints2x2)  
    possibleTwo = show2x2pathsPossible(endpoints2x2, twoGraph)
    print('\n', 'Possible paths'), print(possibleTwo)
    possibleTwo = list(set(possibleTwo))  #  Sets are unordered collections of distinct objects.
    print('\n', 'Removed duplicated with - set'), print(possibleTwo)
    possibleTwo = list(set(possibleTwo).intersection(set(wordlist)))  # Get all words found, that exist in the dictionary
    print('\n', 'Words in Wordlist:'), print(sorted(possibleTwo, key=len)) 

def show3x3pathsPossible(endpoints3x3, threeGraph):
    all_paths = {}
    for item in threeGraph:
	#Result: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        for i in range(1,len(endpoints3x3[item])):
#            start_time = time.time()           
            all_paths.update(find_all_paths_from_to(threeGraph,
                                                    threeGraph[item][0],
                                                    endpoints3x3[item][i]))
#            end_time = time.time() - start_time
#            print('Time used on all paths from ' + threeGraph[item][0] +
#            ' to ' + endpoints3x3[item][i] + ': ' + str(end_time))
    return all_paths


def manualInput3x3(wordlist, ch0, ch1, ch2, ch3, ch4, ch5, ch6, ch7, ch8):
    possibleThree = {}
    threeGraph = make3x3graph(ch0, ch1, ch2, ch3, ch4, ch5, ch6, ch7, ch8)
    endpoints3x3 = makeEndPoints3x3(ch0, ch1, ch2, ch3, ch4, ch5, ch6, ch7, ch8)
    possibleThree = show3x3pathsPossible(endpoints3x3, threeGraph)
    possibleThree = list(set(possibleThree))  #  Sets are unordered collections of distinct objects.
    possibleThree = list(set(possibleThree).intersection(set(wordlist)))  # Get all words found, that exist in the dictionary
    print('\n', 'Words in Wordlist:'), print(sorted(possibleThree, key=len)) # Print list sorted by length        

def show4x4pathsPossible(endpoints4x4, fourGraph):
    all_paths = {}
    for item in fourGraph:
        for i in range(1,len(endpoints4x4[item])):
            all_paths.update(find_all_paths_from_to(fourGraph,
            fourGraph[item][0], endpoints4x4[item][i]))
    return all_paths

def manualInput4x4(wordlist, pos1, pos2, pos3, pos4, pos5, pos6, pos7,
    pos8, pos9, pos10, pos11, pos12, pos13, pos14, pos15, pos16):

    possibleFour = {}
    fourGraph = make4x4graph(pos1, pos2, pos3, pos4, pos5, pos6, pos7,
    pos8, pos9, pos10, pos11, pos12, pos13, pos14, pos15, pos16)
    endpoints4x4 = makeEndPoints4x4(pos1, pos2, pos3, pos4, pos5, pos6,
    pos7, pos8, pos9, pos10, pos11, pos12, pos13, pos14, pos15, pos16)

    start_time = time.time()
    possibleFour = show4x4pathsPossible(endpoints4x4, fourGraph)

    f = open('possibleFour.txt', 'w')
    json.dump(possibleFour, f)
    f.close()

    end_time = time.time() - start_time
    print('\n' + 'Time used on all possible paths for 4x4: '), print(end_time)
    start_time = time.time()
    possibleFour = list(set(possibleFour))  #  Sets are unordered collections of distinct objects.
    end_time = time.time() - start_time
    print('\n' + 'Time used on removing duplicates for 4x4: '), print(end_time)
    start_time = time.time()
    possibleFour = list(set(possibleFour).intersection(set(wordlist)))  # Get all words found, that exist in the dictionary
    end_time = time.time() - start_time
    print('\n' + 'Time used on finding all words in dictionary: '), print(end_time)
    print('\n', 'Words in Wordlist:'), print(sorted(possibleFour, key=len)) # Print list sorted by length        

    f = open('solutionsFour.txt', 'w')
    json.dump(possibleFour, f)
    f.close()

def inputchar(wordlist):
    char = []
    input_str = input('Skriv inn dine bokstaver:' + '\n')
#    word_length = input("Velg ordlengde (A - for alle): ")
#    if word_length == 'A':
#        word_length = 9

    input_str = [x.strip() for x in input_str.split(',')]       # Strip and divide by , and put in a list
#    for letter in input_str:
#        char.append(letter)

    if len(input_str) == 4:
        manualInput2x2(wordlist, input_str[0], input_str[1], input_str[2], input_str[3])
        
    if len(input_str) == 9:
        start_time = time.time()
        manualInput3x3(wordlist, input_str[0], input_str[1], input_str[2], input_str[3], input_str[4], input_str[5], input_str[6], input_str[7], input_str[8])
        end_time = time.time() - start_time
        print('Total time used: '),print(end_time)    

    if len(input_str) == 16:
        start_time = time.time()
        manualInput4x4(wordlist, input_str[0], input_str[1], input_str[2], input_str[3], input_str[4], input_str[5], input_str[6], input_str[7], input_str[8], input_str[9], input_str[10], input_str[11], input_str[12], input_str[13], input_str[14], input_str[15])
        end_time = time.time() - start_time
        print('Time used: '),print(end_time)    

# Run program
inputchar(wordlist)

