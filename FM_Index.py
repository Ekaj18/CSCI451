#FM-Index Implementation

D="$ACGT"

def fm_index(Q,BW,C,occ):
    i = len(Q)-2
    x = Q[i+1]
    st = C[x]+1
    ed = C[D[D.find(x)+1]]
    while st <= ed and i >= 1:
        x = Q[i]
        st = C[x] + occ[(x, st-1)] + 1
        ed = C[x] + occ[(x,ed)]
        i = i - 1
    if st > ed:
        print("Pattern not found")
    else:
        print("["+str(st)+", "+str(ed)+"] is the matching range in the suffix array")

def getSuffix(index):
    return S[index:]

def getBW(index):
    if index == 0:
        return S[len(S)-1]
    return S[index-1]

def build_BW():
    SA = list(range(len(S)))
    SA = sorted(SA, key=getSuffix)
    BW = [getBW(index) for index in SA]
    return BW

def get_Counts():
    C = {}
    for i in range(len(D)):
        if i != 0:
            C[D[i]] = C[D[i - 1]] + S.count(D[i - 1])
        else:
            C[D[i]] = 0
    return C

def build_occ(BW):
    occ = {}
    for c in range(len(D)):
        occ[(D[c],-1)] = 0
    for i in range(len(S)):
        for j in range(len(D)):
            occ[(D[j],i)] = occ[(D[j],i-1)]
        occ[(S[i],i)] += 1
    return occ

print("FM-Search on large test string of 60,000 characters")
file = open("Texts\\text1.txt","r")
S = file.read() + "$"
BW = build_BW()
C = get_Counts()
occ = build_occ(BW)
Q = ["ACTGCGC", "ACTTGGCCCCCCCCCCCCCCCCC", "AAC", "TTTTTGTGTGTGTGTGTG", "CGTAGCCGATATG", "ATGCAAC"]
for q in Q:
    print()
    print("Searching for pattern: " + q)
    fm_index(q,BW,C,occ)
