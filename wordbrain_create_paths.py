def manualInput5x5(wordlist, pos1, pos2, pos3, pos4, pos5, pos6, pos7,
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
