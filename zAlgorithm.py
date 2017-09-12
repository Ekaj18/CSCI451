import time

def zalg(pattern,text):
    endprefix = "$"
    LP = len(pattern)
    TP = len(text)

    # Concatenate
    pattext = pattern + endprefix + text
    LPT = len(pattext)

    Zlist = [0]
    afterPrefix = False
    exactMatches = 0
    zListIndex = []

    l = 0
    r = 0
    for k in range(1,LPT-1): #Start at index two
        if not afterPrefix and pattext[k] == "$":
           afterPrefix = True
        if k>r: # case 1
            i = 0
            ksub = k
            while ksub < LPT and pattext[ksub] == pattext[i]:
                i=i+1
                ksub=ksub+1
            if not afterPrefix :
                Zlist.insert(k,i)
            if LP == i:    # There is an exact match
                exactMatches += 1  # The number of exact matches
                zListIndex.append(k-(LP+1))    # the indeces of those exact matches
            l=k
            r=k+i-1
        else: # else if k <= r -- case 2
            beta = pattext[k:r]
            # position of matching box
            kp = k-l  #kprime or k'
            if Zlist[kp] < len(beta)+1:   # case 2(a)
                if not afterPrefix:
                    Zlist.insert(k,Zlist[kp])    # z value here is the same as before
            else: # case 2(b)
                #compare characters starting at position r+1 to characters starting at position len(beta)+1 until a mismatch occurs
                ksub = len(beta)+1
                i = r+1
                while pattext[ksub] == pattext[i]:
                    i=i+1
                    ksub=ksub+1
                #mismatch occurs at k>=r+1
                if not afterPrefix:
                    Zlist.insert(k, i-k)
                r=i-1
                l=k

    print("The number of exact matches was ", exactMatches)
    return(zListIndex)

PATTERNS = 3
TEXTS = 3
for i in range(1,PATTERNS+1):
    patternFile = open("Patterns/pattern" + str(i) + ".txt", "r")
    pattern = patternFile.read()
    patternFile.close();
    for j in range(1,TEXTS+1):
        textFile = open("Texts/text" + str(j) + ".txt", "r")
        text = textFile.read()
        textFile.close();
        start = time.time()
        output = open("Outputs/output_"+str(i)+"_"+str(j)+".txt","w")
        indices = zalg(pattern, text)
        output.write(",".join(map(str, indices)))
        output.close();
        end = time.time();
        print("Z-Algorithm took", end-start, "seconds to run on pattern", i, "( length", len(pattern),") and text", j, "( length" , len(text), ")");
