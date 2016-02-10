import string
import time
import codecs   # For UTF-8 imports
import json     # For saving to file


def show5x5pathsPossible(endpoints5x5, fiveGraph):
    all_paths = {}
    for item in fiveGraph:
        for i in range(1,len(endpoints5x5[item])):
            all_paths.update(find_all_paths_from_to(fiveGraph,
            fiveGraph[item][0], endpoints5x5[item][i]))
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
