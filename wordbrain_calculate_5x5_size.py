# WORDBRAIN SOLUTION

import string
import time
import codecs   # For UTF-8 imports
import json     # For saving to file
from wordbrain_graphs import *

# variables
wordlist = ''

def find_all_paths_from_to(graph, start, end, path=[]):
    """
    Finds all possible path from startnode to endnode
    Returns: A dictionary
    """
    input_len = 3
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
                    tempText = ''.join([i for i in tempText if not i.isdigit()])
                # Remove all numbers before checking length of string
                if len(tempText) >= input_len:
                    paths.update({tempText: tempText})
                    tempText = ''
    return paths

def show5x5pathsPossible(endpoints5x5, fiveGraph):
    all_paths = {}
    tempPath={}
    for item in fiveGraph:
        for i in range(1,len(endpoints5x5[item])):
            tempPath(find_all_paths_from_to(fiveGraph,
            fiveGraph[item][0], endpoints5x5[item][i]))
            f = open('possibleFiveFrom-' + str(fiveGraph[item][0]) + '-to-' + str(endpoints5x5[item][i]) + '.txt', 'w')
            json.dump(tempPath, f)
            f.close()
            tempPath={}

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
