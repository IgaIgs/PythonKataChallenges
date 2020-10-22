import numpy as np
from operator import itemgetter


def encode(s):
    if s == "":
        result = ("", 0)
        return result

    l = len(s)
    orig = list(s)
    slist = list(s)

    matrixlist = [[0] * l for i in range(l)]
    matrixlist[0] = slist
    for i in range(l - 1):
        shifted = ([slist[-1]] + slist[0:-1])
        matrixlist[i + 1] = shifted
        slist = shifted

    matrixlist.sort()  # sort the 2D array alphabetically
    row_index = matrixlist.index(orig)  # find the row index of the original string

    matrx = np.array(matrixlist)  # represent the 2D array as a matrix
    lastcolumn = (matrx[0:l, -1])  # get the last column of the matrix
    lastcolstr = "".join(lastcolumn)
    result = (lastcolstr, row_index)

    print(result)
    return result


encode('Humble Bundle')


def decode(s, n):
    # if the input string is empty, ignore the index and return empty string
    if s == "":
        return ""

    l = len(s)
    # create a list with tuples containing each of the character and its index in s
    indtuple = sorted([(i, char) for i, char in enumerate(s)], key=itemgetter(1))

    # create new empty array
    shifts = [0 for i in range(l)]
    for pairindex, pair in enumerate(indtuple):
        # assign the index of each char to j and each char to ch
        j, ch = pair
        shifts[j] = pairindex  # assign the indexes of pairs from indtuple to places at j

    index = [n]
    for i in range(1, l):
        # append to the index list the next value from the index which is equal the previous value
        index.append(shifts[index[i - 1]])

    result = [s[i] for i in index]
    result.reverse()
    finalresult = ''.join(result)
    print(finalresult)
    return finalresult


decode('e emnllbduuHB', 2)
