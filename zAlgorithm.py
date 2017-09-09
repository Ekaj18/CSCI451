# Initialize stuff
pattern = "PATTERN"
text = "QWUDQJWNLJWQNRCWEFNPATTERWELJNFLJWENCJWENJKWEWANTTHISPATTERNWEJFNWWEWANTTHISWJEPATTERNFWJEFNW"
endprefix = "5"

LP = len(pattern)
TP = len(text)

# Concatenate
pattext = pattern + endprefix + text
LPT = len(pattext)

Zlist = [0]

exactMatches = 0
zListIndex = []

l = 0
r = 0
for k in range(1,LPT-1):
    if k>r: # case 1
        i = 0
        ksub = k
        while ksub < LPT and pattext[ksub] == pattext[i]:
            i=i+1
            ksub=ksub+1
        Zlist.insert(k,i)
        if LP == i:    # There is an exact match
            exactMatches += 1  # The number of exact matches
            zListIndex.append(k)    # the indeces of those exact matches
        l=k
        r=k+Zlist[k]
    else: # else if k <= r -- case 2
        beta = pattext[k:r]
        # position of matching box
        kp = k-l+1  #kprime or k'
        if Zlist[kp] < len(beta):   # case 2(a)
            Zlist.insert(k,Zlist[kp])    # z value here is the same as before
        else: # case 2(b)
            #compare characters starting at position r+1 to characters starting at position len(beta)+1 until a mismatch occurs
            i = Zlist[kp]
            while pattext[k] == pattext[i]:
                i=i+1
            #mismatch occurs at q>=r+1
            Zlist.insert(k,i-k)
            r=i-1
            l=k

print("The number of exact matches was ", exactMatches, " and the index(es) of the exact matches is/are ", zListIndex)
