class Node():
    def __init__(self, seq_list):
        self.seq_list = []
        self.seq_list.extend(seq_list)
        self.value = None
        self.parent = None
        self.r_child = None
        self.l_child = None

    def set_parent(self, parent):
        self.parent = parent

    def set_children(self, l_child, r_child):
        self.l_child = l_child
        l_child.set_parent(self)
        self.r_child = r_child
        r_child.set_parent(self)

    def set_value(self, value):
        self.value = value

    def get_seq_list(self):
        return list(self.seq_list)

    def get_value(self):
        return self.value

    def get_l_child(self):
        return self.l_child;

    def get_r_child(self):
        return self.r_child

    def print_tree(self, num=0):
        print("Label: " + str(self.value))
        print(str(num) + ": " + str(self.seq_list))
        print()
        if self.l_child != None:
            self.l_child.print_tree(num+1)
        if self.r_child != None:
            self.r_child.print_tree(num+1)
    

def score(i, j):
    if i is j:
        return 0
    else:
        return -1

def pairwise_edit_distance(s, t):
    v = [[0 for i in range(len(t)+1)] for j in range(len(s)+1)]
    for i in range(1,len(s)+1):
        for j in range(1,len(t)+1):
            v[i][j] = max( v[i-1][j-1] + score(s[i-1],t[j-1]),
                           v[i-1][j] + score(s[i-1]," "),
                           v[i][j-1] + score(" ",t[j-1]))
    return v[len(s)][len(t)]


def create_dist_matrix(slist):
    d = [[0 for i in range(len(slist))] for j in range(len(slist))]
    for i in range(len(slist)):
        for j in range(i,len(slist)):
            if i != j:
                d[i][j] = pairwise_edit_distance(slist[i],slist[j])
                d[j][i] = d[i][j]
    return d

def create_tree_from_dist_matrix(slist, d):
    size = len(slist)
    nodes = []
    for i in range(size):
        n_list = []
        n_list.append(i)
        n = Node(n_list)
        n.set_value(list(list(j) for j in slist[i]))
        nodes.append(n)

    while len(nodes) > 1:
        min_dist = -1000000
        min_loc = [-1,-1]
        for i in range(len(nodes)):
            for j in range(i,len(nodes)):
                if i != j:
                    dist_list = []
                    for n in nodes[i].get_seq_list():
                        for m in nodes[j].get_seq_list():
                            dist_list.append(d[n][m])
                    dist = sum(dist_list) / len(dist_list)
                    if dist > min_dist:
                        min_dist = dist
                        min_loc = [i,j]
        n1 = nodes[min_loc[0]]
        n2 = nodes[min_loc[1]]
        n_list = n1.get_seq_list()
        n_list.extend(n2.get_seq_list())
        n = Node(n_list)
        n.set_children(n1, n2)
        nodes.remove(n1)
        nodes.remove(n2)
        nodes.append(n)
    n = nodes[0]
    return n
    
def fitch_algorithm(node):
    if node.get_l_child() == None and node.get_r_child() ==  None:
        return node.get_value()
    else:
        left = []
        right = []
        if node.get_l_child() != None:
            left = fitch_algorithm(node.get_l_child())
        if node.get_r_child() != None:
            right = fitch_algorithm(node.get_r_child())
        cur = [[] for i in range(len(left))]
        for i in range(len(left)):
            for j in range(len(left[i])):
                if left[i][j] in right[i]:
                    cur[i].append(left[i][j])
            if len(cur[i]) == 0:
                cur[i] = list(left[i])
                cur[i].extend(right[i])
            cur[i] = list(set(cur[i]))
        node.set_value(cur)
        return cur
        
def simplify_tree(node):
    if node.get_l_child() != None and node.get_r_child() !=  None:
        new_value = [[] for i in range(len(node.get_value()))]
        cur = node.get_value()
        left = node.get_l_child().get_value()
        right = node.get_r_child().get_value()
        for i in range(len(cur)):
            match = False
            for j in range(len(cur[i])):
                if cur[i][j] in right[i] and cur[i][j] in left[i]:
                    match = True
                    new_value[i].append(cur[i][j])
            if not match:
                new_value[i] = cur[i]

        node.set_value(new_value)
        simplify_tree(node.get_l_child())
        simplify_tree(node.get_r_child())            
    

slist = ["ACTG", "GTCA", "TTTA", "GGCA"]
d = create_dist_matrix(slist)
root = create_tree_from_dist_matrix(slist, d)
fitch_algorithm(root)
simplify_tree(root)
root.print_tree()
