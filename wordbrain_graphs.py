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