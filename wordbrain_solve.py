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



start_time = time.time()
manualInput4x4(wordlist, 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p')
end_time = time.time() - start_time
print('Time used: '),print(end_time)    
