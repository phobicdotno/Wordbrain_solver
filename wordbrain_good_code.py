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

def loadDict3():
    file = open('wordDictStart3.txt', 'r', encoding='utf-8-sig')
    wordDictStart3 = json.load(file)
    file.close()
    return wordDictStart3


def find_all_paths_from_to(graph, start, end, wordDictStart3, path=[]):
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
            newpaths = find_all_paths_from_to(graph, node, end, wordDictStart3, path)
            for newpath in newpaths:
                for char in newpath:
                    tempText+=''.join(char.lstrip('[]'))
                    tempText = ''.join([i for i in tempText if not i.isdigit()]) # Remove all numbers before checking length of string
                print('Text found:' + tempText)    
                if len(tempText) > 2:
                    print(tempText + ' ' + tempText[0:3] + ' ' + str(tempText[0:3] in wordDictStart3))
                    if wordDictStart3[tempText[0:3]]:
                        paths.update({tempText: tempText})
                tempText = ''
            


    return paths

