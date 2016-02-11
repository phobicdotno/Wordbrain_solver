# WORDBRAIN - Gererates all possible 4x4 paths

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

def show4x4pathsPossible(endpoints4x4, fourGraph):
    all_paths = {}
    for item in fourGraph:
        f = open('possibleFourFrom-' + str(fourGraph[item][0]) + '.txt', 'w')
        for i in range(1,len(endpoints4x4[item])):
            print('Started ' + str(item) + ' to ' + str(endpoints4x4[item][i])) 
            all_paths.update(find_all_paths_from_to(fourGraph, fourGraph[item][0], endpoints4x4[item][i]))
        json.dump(all_paths, f)
        f.close()
        print('Created: possibleFourFrom-' + str(fourGraph[item][0]) + '.txt\n' )
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


manualInput4x4(wordlist, 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p')
