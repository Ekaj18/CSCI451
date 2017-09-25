#   Smith-Waterman Algorithm
#   CSCI 451, HW 2 Problem 1
#   Emerald Ellis, Elizabeth Pennell, and Jake Petek

s = "bbbtat"
t = "ctgtacter"

#setup value array
v = [[[0, " "] for i in range(len(t)+1)] for j in range(len(s)+1)]

#scoring function
def score(i,j):
    if i is j:
        return 2
    else:
        return -1

#variables to keep track of the highest score and its location    
topscore = 0;
loc = [0,0];
for i in range(1,len(s)+1):
    for j in range(1,len(t)+1):
        max = 0
        dir = " "
        #score for a diagonal move
        diag = v[i-1][j-1][0] + score(s[i-1],t[j-1])
        #score for a move from above
        up = v[i-1][j][0] + score(s[i-1]," ")
        #score for a move from the left
        left = v[i][j-1][0] + score(" ",t[j-1])
        if diag >= max:
            dir = "d"
            max = diag
        if up >= max:
            if up == max:
                dir += "u"
            else:
                dir = "u"
                max = up
        if left >= max:
            if left == max:
                dir += "l"
            else:
                dir = "l"
                max = left
        v[i][j] = [max, dir]
        if max > topscore:
           topscore = max
           loc = [i,j]
        #v[i][j][0] = max(0,
        #              v[i-1][j-1][0] + score(s[i-1],t[j-1]),
        #              v[i-1][j][0] + score(s[i-1]," "),
        #              v[i][j-1][0] + score(" ",t[j-1]))

#prints complete matrix
#for i in range(len(v)):
#   print(v[i])

s_align = ""
t_align = ""
#set starting location based on topscore
i = loc[0]
j = loc[1]
#find alignment using matrix
while i>0 or j>0:
    if "d" in v[i][j][1]:
        i-=1
        j-=1
        s_align = s[i] + s_align
        t_align = t[j] + t_align
    elif "l" in v[i][j][1]:
        j-=1
        s_align = "_" + s_align
        t_align = t[j] + t_align
    elif "u" in v[i][j][1]:
        i-=1
        s_align = s[i] + s_align
        t_align = "j" + t_align
    else:
        i = 0
        j = 0

print(s_align)
print(t_align)
