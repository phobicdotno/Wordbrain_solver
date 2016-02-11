def make2x2graph(pos1, pos2, pos3, pos4):                               
    """
    Returns a tree as dictionary with startnode as key.
    First value is same as startnode, and the rest is neighbour nodes

    pos1  -   pos2
      |   X     |
    pos3  -   pos4

    """
    return {pos1: [pos1, pos2, pos3, pos4],
            pos2: [pos2, pos4, pos3, pos1],
            pos3: [pos3, pos1, pos2, pos4],
            pos4: [pos4, pos3, pos1, pos2]}                   

def makeEndPoints2x2(pos1, pos2, pos3, pos4):
    """
    Possible endpoints from startpoint on 2x2
    Get value with endpoints[key][item]
    """
    return {pos1: [pos1, pos2, pos3, pos4],
            pos2: [pos2, pos4, pos3, pos1],
            pos3: [pos3, pos1, pos2, pos4],
            pos4: [pos4, pos3, pos1, pos2]}     


def make3x3graph(pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9):
    """
    Returns a dictionary with startnode as key.
    First value is same as startnode, and the rest is neighbour nodes

     pos1  -   pos2  -   pos3
      |    X     |   X     |
     pos4  -   pos5  -   pos6
      |    X     |   X     |
     pos7  -   pos8  -   pos9

    """
    return {pos1: [pos1, pos2, pos5, pos4],
            pos2: [pos2, pos3, pos6, pos5, pos4, pos1],
            pos3: [pos3, pos6, pos5, pos2],
            pos4: [pos4, pos1, pos2, pos5, pos8, pos7],
            pos5: [pos5, pos1, pos2, pos3, pos6, pos9, pos8, pos7, pos4],
            pos6: [pos6, pos2, pos3, pos9, pos8, pos5],
            pos7: [pos7, pos4, pos5, pos8],
            pos8: [pos8, pos4, pos5, pos6, pos9, pos7],
            pos9: [pos9, pos5, pos6, pos8]}

def makeEndPoints3x3(pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9):
    """
    Possible endpoints from startpoint on 3x3
    First value is Start node.
    """
    return  {pos1: [pos1,pos2,pos3,pos4,pos5,pos6,pos7,pos8,pos9],
             pos2: [pos2,pos1,pos3,pos4,pos5,pos6,pos7,pos8,pos9],
             pos3: [pos3,pos1,pos2,pos4,pos5,pos6,pos7,pos8,pos9],
             pos4: [pos4,pos1,pos2,pos3,pos5,pos6,pos7,pos8,pos9],
             pos5: [pos5,pos1,pos2,pos3,pos4,pos6,pos7,pos8,pos9],
             pos6: [pos6,pos1,pos2,pos3,pos4,pos5,pos7,pos8,pos9],
             pos7: [pos7,pos1,pos2,pos3,pos4,pos5,pos6,pos8,pos9],
             pos8: [pos8,pos1,pos2,pos3,pos4,pos5,pos6,pos7,pos9],
             pos9: [pos9,pos1,pos2,pos3,pos4,pos5,pos6,pos7,pos8]}

def make4x4graph(pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9, pos10, pos11, pos12, pos13, pos14, pos15, pos16):
    """
    Returns a dictionary with startnode as key.
    First value is same as startnode, and the rest is neighbour nodes

     pos1  -   pos2  -   pos3  -   pos4
      |    X     |   X     |   X     |
     pos5  -   pos6  -   pos7  -   pos8
      |    X     |   X     |   X     |
     pos9  -  pos10  -  pos11  -   pos12
      |    X     |   X     |   X     |
    pos13  -  pos14  -  pos15  -   pos16

    """
    return { pos1: [pos1, pos2, pos6, pos5],
             pos2: [pos2, pos1, pos3, pos7, pos6, pos5],
             pos3: [pos3, pos2, pos4, pos8, pos7, pos6],
             pos4: [pos4, pos3, pos8, pos7],
             pos5: [pos5, pos1, pos2, pos6, pos10, pos9],
             pos6: [pos6, pos1, pos2, pos3, pos7, pos11, pos10, pos9, pos5],
             pos7: [pos7, pos2, pos3, pos4, pos8, pos12, pos11, pos10, pos6],
             pos8: [pos8, pos3, pos4, pos12, pos11, pos7],
             pos9: [pos9, pos5, pos6, pos10, pos14, pos13],
            pos10: [pos10, pos5, pos6, pos7, pos11, pos15, pos14, pos13, pos9],
            pos11: [pos11, pos6, pos7, pos8, pos12, pos16, pos15, pos14, pos10],
            pos12: [pos12, pos7, pos8, pos16, pos15, pos11],
            pos13: [pos13, pos9, pos10, pos14],
            pos14: [pos14, pos9, pos10, pos11, pos15, pos13],
            pos15: [pos15, pos10, pos11, pos12, pos16, pos14],
            pos16: [pos16, pos11, pos12, pos15]}

def makeEndPoints4x4(pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9, pos10, pos11, pos12, pos13, pos14, pos15, pos16):
    """
    Possible endpoints from startpoint on 4x4
    First value is Start node.
    """
    return  { pos1: [pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9, pos10, pos11, pos12, pos13, pos14, pos15, pos16],
              pos2: [pos2, pos1, pos3, pos4, pos5, pos6, pos7, pos8, pos9, pos10, pos11, pos12, pos13, pos14, pos15, pos16],
              pos3: [pos3, pos1, pos2, pos4, pos5, pos6, pos7, pos8, pos9, pos10, pos11, pos12, pos13, pos14, pos15, pos16],
              pos4: [pos4, pos1, pos2, pos3, pos5, pos6, pos7, pos8, pos9, pos10, pos11, pos12, pos13, pos14, pos15, pos16],
              pos5: [pos5, pos1, pos2, pos3, pos4, pos6, pos7, pos8, pos9, pos10, pos11, pos12, pos13, pos14, pos15, pos16],
              pos6: [pos6, pos1, pos2, pos3, pos4, pos5, pos7, pos8, pos9, pos10, pos11, pos12, pos13, pos14, pos15, pos16],
              pos7: [pos7, pos1, pos2, pos3, pos4, pos5, pos6, pos8, pos9, pos10, pos11, pos12, pos13, pos14, pos15, pos16],
              pos8: [pos8, pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos9, pos10, pos11, pos12, pos13, pos14, pos15, pos16],
              pos9: [pos9, pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos10, pos11, pos12, pos13, pos14, pos15, pos16],
             pos10: [pos10, pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9, pos11, pos12, pos13, pos14, pos15, pos16],
             pos11: [pos11, pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9, pos10, pos12, pos13, pos14, pos15, pos16],
             pos12: [pos12, pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9, pos10, pos11, pos13, pos14, pos15, pos16],
             pos13: [pos13, pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9, pos10, pos11, pos12, pos14, pos15, pos16],
             pos14: [pos14, pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9, pos10, pos11, pos12, pos13, pos15, pos16],
             pos15: [pos15, pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9, pos10, pos11, pos12, pos13, pos14, pos16],
             pos16: [pos16, pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9, pos10, pos11, pos12, pos13, pos14, pos15]}

def make5x5graph(pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9, pos10, pos11, pos12, pos13, pos14, pos15, pos16, pos17, pos18, pos19, pos20, pos21, pos22, pos23, pos24, pos25):
    """
    Returns a dictionary with startnode as key.
    First value is same as startnode, and the rest is neighbour nodes

     pos1  -   pos2  -   pos3  -   pos4  -   pos5
      |    X     |   X     |   X     |   X     |
     pos6  -   pos7  -   pos8  -   pos9  -   pos10
      |    X     |   X     |   X     |   X     |
    pos11  -  pos12  -  pos13  -  pos14  -   pos15
      |    X     |   X     |   X     |   X     |
    pos16  -  pos17  -  pos18  -  pos19  -   pos20
      |    X     |   X     |   X     |   X     |
    pos21  -  pos22  -  pos23  -  pos24  -   pos25

    """
    return { pos1: [pos1, pos2, pos7, pos6],
             pos2: [pos2, pos1, pos3, pos8, pos7, pos6],
             pos3: [pos3, pos2, pos4, pos9, pos8, pos7],
             pos4: [pos4, pos3, pos5, pos10, pos9, pos8],
             pos5: [pos5, pos4, pos10, pos9],
             pos6: [pos6, pos1, pos2, pos7, pos12, pos12],
             pos7: [pos7, pos1, pos2, pos3, pos8, pos13, pos12, pos11, pos6],
             pos8: [pos8, pos2, pos3, pos4, pos9, pos14, pos13, pos12, pos7],
             pos9: [pos9, pos3, pos4, pos5, pos10, pos15, pos14, pos13, pos8],
            pos10: [pos10, pos4, pos5, pos15, pos14, pos9],
            pos11: [pos11, pos6, pos7, pos12, pos17, pos16],
            pos12: [pos12, pos6, pos7, pos8, pos13, pos18, pos17, pos16, pos11],
            pos13: [pos13, pos7, pos8, pos9, pos14, pos19, pos18, pos17, pos12],
            pos14: [pos14, pos8, pos9, pos10, pos15, pos20, pos19, pos18, pos13],
            pos15: [pos15, pos9, pos10, pos20, pos19, pos14],
            pos16: [pos16, pos11, pos12, pos17, pos22, pos21],
            pos17: [pos17, pos11, pos12, pos13, pos18, pos23],
            pos18: [pos18, pos12, pos13, pos14, pos19, pos24, pos23, pos22, pos17],
            pos19: [pos19, pos13, pos14, pos15, pos20, pos25, pos24, pos23, pos18],
            pos20: [pos20, pos14, pos15, pos25, pos24, pos19],
            pos21: [pos21, pos16, pos17, pos22],
            pos22: [pos22, pos16, pos17, pos18, pos23, pos21],
            pos23: [pos23, pos17, pos18, pos19, pos24, pos22],
            pos24: [pos24, pos18, pos19, pos20, pos25, pos23],
            pos25: [pos25, pos19, pos20, pos24]}

def makeEndPoints5x5(pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9, pos10, pos11, pos12, pos13, pos14, pos15, pos16, pos17, pos18, pos19, pos20, pos21, pos22, pos23, pos24, pos25):
    """
    Possible endpoints from startpoint on 5x5
    First value is Start node.
    """
    return  { pos1: [pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9, pos10, pos11, pos12, pos13, pos14, pos15, pos16, pos17, pos18, pos19, pos20, pos21, pos22, pos23, pos24, pos25],
              pos2: [pos2, pos1, pos3, pos4, pos5, pos6, pos7, pos8, pos9, pos10, pos11, pos12, pos13, pos14, pos15, pos16, pos17, pos18, pos19, pos20, pos21, pos22, pos23, pos24, pos25],
              pos3: [pos3, pos2, pos1, pos4, pos5, pos6, pos7, pos8, pos9, pos10, pos11, pos12, pos13, pos14, pos15, pos16, pos17, pos18, pos19, pos20, pos21, pos22, pos23, pos24, pos25],
              pos4: [pos4, pos3, pos2, pos1, pos5, pos6, pos7, pos8, pos9, pos10, pos11, pos12, pos13, pos14, pos15, pos16, pos17, pos18, pos19, pos20, pos21, pos22, pos23, pos24, pos25],
              pos5: [pos5, pos4, pos3, pos2, pos1, pos6, pos7, pos8, pos9, pos10, pos11, pos12, pos13, pos14, pos15, pos16, pos17, pos18, pos19, pos20, pos21, pos22, pos23, pos24, pos25],
              pos6: [pos6, pos5, pos4, pos3, pos2, pos1, pos7, pos8, pos9, pos10, pos11, pos12, pos13, pos14, pos15, pos16, pos17, pos18, pos19, pos20, pos21, pos22, pos23, pos24, pos25],
              pos7: [pos7, pos6, pos5, pos4, pos3, pos2, pos1, pos8, pos9, pos10, pos11, pos12, pos13, pos14, pos15, pos16, pos17, pos18, pos19, pos20, pos21, pos22, pos23, pos24, pos25],
              pos8: [pos8, pos7, pos6, pos5, pos4, pos3, pos2, pos1, pos9, pos10, pos11, pos12, pos13, pos14, pos15, pos16, pos17, pos18, pos19, pos20, pos21, pos22, pos23, pos24, pos25],
              pos9: [pos9, pos8, pos7, pos6, pos5, pos4, pos3, pos2, pos1, pos10, pos11, pos12, pos13, pos14, pos15, pos16, pos17, pos18, pos19, pos20, pos21, pos22, pos23, pos24, pos25],
             pos10: [pos10, pos9, pos8, pos7, pos6, pos5, pos4, pos3, pos2, pos1, pos11, pos12, pos13, pos14, pos15, pos16, pos17, pos18, pos19, pos20, pos21, pos22, pos23, pos24, pos25],
             pos11: [pos11, pos10, pos9, pos8, pos7, pos6, pos5, pos4, pos3, pos2, pos1, pos12, pos13, pos14, pos15, pos16, pos17, pos18, pos19, pos20, pos21, pos22, pos23, pos24, pos25],
             pos12: [pos12, pos11, pos10, pos9, pos8, pos7, pos6, pos5, pos4, pos3, pos2, pos1, pos13, pos14, pos15, pos16, pos17, pos18, pos19, pos20, pos21, pos22, pos23, pos24, pos25],
             pos13: [pos13, pos12, pos11, pos10, pos9, pos8, pos7, pos6, pos5, pos4, pos3, pos2, pos1, pos14, pos15, pos16, pos17, pos18, pos19, pos20, pos21, pos22, pos23, pos24, pos25],
             pos14: [pos14, pos13, pos12, pos11, pos10, pos9, pos8, pos7, pos6, pos5, pos4, pos3, pos2, pos1, pos15, pos16, pos17, pos18, pos19, pos20, pos21, pos22, pos23, pos24, pos25],
             pos15: [pos15, pos14, pos13, pos12, pos11, pos10, pos9, pos8, pos7, pos6, pos5, pos4, pos3, pos2, pos1, pos16, pos17, pos18, pos19, pos20, pos21, pos22, pos23, pos24, pos25],
             pos16: [pos16, pos15, pos14, pos13, pos12, pos11, pos10, pos9, pos8, pos7, pos6, pos5, pos4, pos3, pos2, pos1, pos17, pos18, pos19, pos20, pos21, pos22, pos23, pos24, pos25],
             pos17: [pos17, pos16, pos15, pos14, pos13, pos12, pos11, pos10, pos9, pos8, pos7, pos6, pos5, pos4, pos3, pos2, pos1, pos18, pos19, pos20, pos21, pos22, pos23, pos24, pos25],
             pos18: [pos18, pos17, pos16, pos15, pos14, pos13, pos12, pos11, pos10, pos9, pos8, pos7, pos6, pos5, pos4, pos3, pos2, pos1, pos19, pos20, pos21, pos22, pos23, pos24, pos25],
             pos19: [pos19, pos18, pos17, pos16, pos15, pos14, pos13, pos12, pos11, pos10, pos9, pos8, pos7, pos6, pos5, pos4, pos3, pos2, pos1, pos20, pos21, pos22, pos23, pos24, pos25],
             pos20: [pos20, pos19, pos18, pos17, pos16, pos15, pos14, pos13, pos12, pos11, pos10, pos9, pos8, pos7, pos6, pos5, pos4, pos3, pos2, pos1, pos21, pos22, pos23, pos24, pos25],
             pos21: [pos21, pos20, pos19, pos18, pos17, pos16, pos15, pos14, pos13, pos12, pos11, pos10, pos9, pos8, pos7, pos6, pos5, pos4, pos3, pos2, pos1, pos22, pos23, pos24, pos25],
             pos22: [pos22, pos21, pos20, pos19, pos18, pos17, pos16, pos15, pos14, pos13, pos12, pos11, pos10, pos9, pos8, pos7, pos6, pos5, pos4, pos3, pos2, pos1, pos23, pos24, pos25],
             pos23: [pos23, pos22, pos21, pos20, pos19, pos18, pos17, pos16, pos15, pos14, pos13, pos12, pos11, pos10, pos9, pos8, pos7, pos6, pos5, pos4, pos3, pos2, pos1, pos24, pos25],
             pos24: [pos24, pos23, pos22, pos21, pos20, pos19, pos18, pos17, pos16, pos15, pos14, pos13, pos12, pos11, pos10, pos9, pos8, pos7, pos6, pos5, pos4, pos3, pos2, pos1, pos25],
             pos25: [pos25, pos24, pos23, pos22, pos21, pos20, pos19, pos18, pos17, pos16, pos15, pos14, pos13, pos12, pos11, pos10, pos9, pos8, pos7, pos6, pos5, pos4, pos3, pos2, pos1]}
              
