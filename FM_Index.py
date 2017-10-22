#FM-Index Implementation
#S="acgtgccta$"
D="$acgt"
def fm_index(Q,BW,C,occ):
    x = Q[end]
    i = len(Q)-1
    st = C[x]+1
    ed = C[x+1]
    while st <= ed and i >= 1:
        x = Q[i]
        st = C[x] + occ(x, st-1) + 1
        ed = C[x] + occ(x,ed)
        i = i - 1
    if st > ed:
        print("No valid comparisons")
    else:
        print("["+str(st)+", "+str(ed)+"] is the parameter for a match")

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
    C = {}
    for i in range(len(D)):
        if i!= 0:
            C[D[i]] = C[D[i-1]] + S.count(D[i-1])
        else:
            C[D[i]] = 0
    print(C)

file = open("text.txt","r")
S = file.read() + "$"
S = S.lower()
build_BW()
