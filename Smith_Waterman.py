#   Smith-Waterman Algorithm
#   CSCI 451, HW 2 Problem 1
#   Emerald Ellis, Elizabeth Pennell, and Jake Petek

s = "tgt"
t = "ctgtact"
slen = len(s)+1
tlen=len(t)+1
v = [[0 for item in range(tlen)] for i in range(slen)]

def match(s,t):
    if s is t:
        return 2
    else:
        return -1

def smith_waterman(s, t):
    i = len(s)
    j = len(t)
    # a of s and b of t have highest global alignment score
    # V(i,j) is max score of the global alignment of A and B over S and T
    # Base case:
    if i is 0:
        v[i][j] = 0
        if j is 0:
            v[i][j] = 0
        return v
    elif j is 0:
        v[i][j] = 0
        return v
    else:
        one = 0
        v2 =smith_waterman(s[:i-1],t[:j-1])
        mat = match(s[i-1],t[j-1])
        two = v2[i-1][j-1]+mat
        v3 = smith_waterman(s[:i-1],t[:j])
        three = v3[i-1][j]-1
        v4 = smith_waterman(s[:i],t[:j-1])
        four = v4[i][j-1]-1
        v[i][j] = max(one, two, three, four)
        return v
        
v = smith_waterman(s,t)
print(v)
print(max(max(v)))
