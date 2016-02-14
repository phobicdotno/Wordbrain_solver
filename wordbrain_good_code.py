WORDLIST_FILENAME = "bokmaal_2-9-bokst.txt"
#WORDLIST_FILENAME = "test.txt"
import json


def loadWords():
    """
    Loads all the words from the dictionary
    """
    print("Loading word list from file...")
    wordlist = [line.rstrip('\n') for line in open(WORDLIST_FILENAME, encoding='utf-8-sig')]
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def loadDict(dictFile):
    file = open(dictFile, 'r', encoding='utf-8-sig')
    wordDictionary = json.load(file)
    file.close()
    return wordDictionary


def find_all_paths_from_to(graph, start, end, wordDictionary, path=[]):
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
            newpaths = find_all_paths_from_to(graph, node, end, wordDictionary, path)
            for newpath in newpaths:
                for char in newpath:
                    tempText+=''.join(char.lstrip('[]'))
                    tempText = ''.join([i for i in tempText if not i.isdigit()]) # Remove all numbers before checking length of string
                # print('Text found: ' + tempText + ' - ' + str(tempText in wordDictionary))    # DEBUG
                if tempText in wordDictionary:
                    paths.update({tempText: tempText})
                else:
                    paths.update({})
                tempText = ''
            


    return paths

# manualInput3x3(wordlist, 'f','t1','s','a','e1','e2','t2','t3','t4', wordDictionary)    # DEBUG

