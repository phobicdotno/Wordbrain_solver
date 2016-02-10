WORDLIST_FILENAME = "bokmaal_2-9-bokst.txt"
#WORDLIST_FILENAME = "test.txt"

def loadWords():
    """
    Loads all the words from the dictionary
    """
    print("Loading word list from file...")
    wordlist = [line.rstrip('\n') for line in open(WORDLIST_FILENAME, encoding='utf-8-sig')]
    print("  ", len(wordlist), "words loaded.")
    return wordlist

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

