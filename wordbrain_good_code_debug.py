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


def find_all_paths_from_to(graph, start, end, wordDictionary, wordDictionaryFirst3, path=[]):
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
        # Value example: ['t3', 'a', 'e1', 's', 'e2', 't4']
        tempNode = ''.join([i for i in path])   # Convert dict to string with numbering
        tempNode = ''.join([i for i in tempNode if not i.isdigit()])    # Remove numbers
        # Value example: taeset
        print(tempNode)
        if node not in path:
            newpaths = find_all_paths_from_to(graph, node, end, wordDictionary, wordDictionaryFirst3, path)

            for newpath in newpaths:
                for char in newpath:
                    tempText+=''.join(char.lstrip('[]'))
                    tempText = ''.join([i for i in tempText if not i.isdigit()]) # Remove all numbers before checking length of string
                if tempText in wordDictionary:
                    paths.update({tempText: tempText})
                    #print(tempText)
                tempText = ''
    return paths

# manualInput3x3(wordlist, 'f','t1','s','a','e1','e2','t2','t3','t4', wordDictionary, wordDictionaryFirst3)    # DEBUG

#  s1,g1,f1,t1,t2,e1,r1,1b,ø1,l1,a1,e2,v,i,m,s2
