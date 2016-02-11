# WORDBRAIN - Generates all possible 5x5 paths

import string
import time
import codecs   # For UTF-8 imports
import json     # For saving to file
from wordbrain_graphs import *
from wordbrain_good_code import *

# variables
wordlist = ''

def find_all_paths_from_to(graph, start, end, path=[]):
    """
    Finds all possible path from startnode to endnode
    Returns: A dictionary
    """
    path = path + [start]
    if start == end:
        return [path]
    if not start in graph:
        return []
    paths = {}
    tempText = ''
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths_from_to(graph, node, end, path)
            for newpath in newpaths:
                for char in newpath:
                    tempText+=''.join(char.lstrip('[]'))
                paths.update({tempText: tempText})
                tempText = ''
    return paths

def show5x5pathsPossible(endpoints5x5, fiveGraph):
    all_paths = {}
    for item in fiveGraph:
        f = open('possibleFiveFrom-' + str(fiveGraph[item][0]) + '.txt', 'w')
        for i in range(1,len(endpoints5x5[item])):
            print('Started ' + str(item) + ' to ' + str(endpoints5x5[item][i]))         # How far we are
            start_time = time.time()
            all_paths = find_all_paths_from_to(fiveGraph, fiveGraph[item][0], endpoints5x5[item][i])
            end_time = time.time() - start_time
            print('\n' + 'Time used on finding paths: ' + str(end_time))
        print('Possible paths: ' + str(len(all_paths)))
        json.dump(all_paths, f)
        f.close()
        print('Created: possibleFiveFrom-' + str(fiveGraph[item][0]) + '.txt\n' )
    return all_paths

def manualInput5x5(wordlist, pos1, pos2, pos3, pos4, pos5, pos6, pos7,
pos8, pos9, pos10, pos11, pos12, pos13, pos14, pos15, pos16, pos17,
pos18, pos19, pos20, pos21, pos22, pos23, pos24, pos25):

    possibleFive = {}

    fiveGraph = make5x5graph(pos1, pos2, pos3, pos4, pos5, pos6, pos7,
    pos8, pos9, pos10, pos11, pos12, pos13, pos14, pos15, pos16, pos17,
    pos18, pos19, pos20, pos21, pos22, pos23, pos24, pos25)

    endpoints5x5 = makeEndPoints5x5(pos1, pos2, pos3, pos4, pos5, pos6,
    pos7, pos8, pos9, pos10, pos11, pos12, pos13, pos14, pos15, pos16,
    pos17, pos18, pos19, pos20, pos21, pos22, pos23, pos24, pos25)

    possibleFive = show5x5pathsPossible(endpoints5x5, fiveGraph)


print(manualInput5x5(wordlist, 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z'))
