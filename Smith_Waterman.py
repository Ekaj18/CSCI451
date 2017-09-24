#   Smith-Waterman Algorithm
#   CSCI 451, HW 2 Problem 1
#   Emerald Ellis, Elizabeth Pennell, and Jake Petek

def match(s,t):
    if s is t:
        return 2
    else:
        return -1

def smith_waterman(s, t):
    i = len(s)
    j = len(t)
    v = [[0 for x in range(i)] for y in range(j)]
    # a of s and b of t have highest global alignment score
    # V(i,j) is max score of the global alignment of A and B over S and T
    # Base case:
    if i is 0:
        v[0][j] = 0
        return v
    elif j is 0:
        v[i][0] = 0
        return v
    else:
        one = 0
        two = smith_waterman(s[:i-1],t[:j-1])[i-1][j-1]+match(s[i],t[j])
        three = smith_waterman(s[:i-1],t[:j])[i-1][j]-1
        four = smith_waterman(s[:i],t[:j-1])[i][j-1]-1
        v[i][j] = max(one, two, three, four)
        return v
        
s = "act"
t = "ctg"
v = smith_waterman(s,t)
