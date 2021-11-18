"""
Math 560
Project 4
Fall 2021

Partner 1: Amy Wang (pw137)
Partner 2: Lu Liu (ll394)
Date:
"""

# Import p4tests.
from p4tests import *

################################################################################

"""
ED: the edit distance function
input:
src: the original string
dest: the string which we need to convert to
output:
minimum number of edits that needs to use and the specific converting steps.
"""

def ED(src, dest, prob='ED'):
    # Check the problem to ensure it is a valid choice.
    if (prob != 'ED') and (prob != 'ASM'):
        raise Exception('Invalid problem choice!')

    dist = 0 # This is a placeholder, remove and implement!
    edits = [] # This is a placeholder, remove and implement!

#first, initialize the table

    n = len(src)
    m = len(dest)
    dpTable = [[None for j in range(m+1)] for i in range(n+1)]

#fill in the base cases(first row and first column)

    for i in range(n+1):
        dpTable[i][0] = i
    for j in range(m+1):
        dpTable[0][j] = j

#fill in the table by iterating each row.
    for i in range(1,n+1):
        for j in range(1,m+1):
#if letters are the same, copy the diagonal
            if src[i-1] == dest[j-1]:
                dpTable[i][j] = dpTable[i-1][j-1]
#if not same, do minimize computation
            else:
                delete = dpTable[i-1][j]
                insert = dpTable[i][j-1]
                sub = dpTable[i-1][j-1]
                dpTable[i][j] = 1 + min([delete, insert, sub])
                
                
                
    return dist, edits

################################################################################

"""
Main function.
"""
if __name__ == "__main__":
    edTests(False)
    print()
    compareGenomes(True, 30, 300, 'ED')
    print()
    compareRandStrings(True, 30, 300, 'ED')
    print()
    compareGenomes(True, 30, 300, 'ASM')
    print()
    compareRandStrings(True, 30, 300, 'ASM')
