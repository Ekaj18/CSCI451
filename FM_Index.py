#FM-Index Implementation

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
        
