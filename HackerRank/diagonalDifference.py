from hmac import digest


arr = [[11, 2, 4],[4, 5, 6],[10, 8, -12]]


# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    diagonal1 = 0
    diagonal2 = 0
    le = len(arr)
    l = le-1
    for i in range( le ):
        diagonal1 = diagonal1 + (arr[i][i])
        diagonal2 = diagonal2 + (arr[i][l])
        l= l-1
    print(abs(diagonal1-diagonal2))

diagonalDifference(arr)