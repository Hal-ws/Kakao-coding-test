import sys


def solution(nodeinfo):
    global result1, result2, tree
    l = len(nodeinfo) # node의 갯수
    sys.setrecursionlimit(10 ** 6)
    result1, result2 = [], []
    idxBook = {} # 노드의 nodeinfo 안에서의 idx 저장
    lBound, rBound = 0, 0
    tree = [[None, None] for i in range(l + 1)] # i + 1 번 노드의 왼쪽, 오른쪽 자식노드 정리
    for i in range(l):
        nodeinfo[i] = [nodeinfo[i][1], nodeinfo[i][0], i + 1, None] # y, x 노드번호, 노드 level
        if nodeinfo[i][1] > rBound:
            rBound = nodeinfo[i][1]
    nodeinfo.sort(reverse=True)
    for i in range(l):
        node = nodeinfo[i][2]
        idxBook[node] = i
    root = nodeinfo[0][2] # root node의 번호
    nodeinfo[idxBook[root]][3] = 0
    nodes = [[root]] # level에 따른 node 저장
    level = 0
    for i in range(1, l):
        lastNode = nodes[level][0]
        lasty = nodeinfo[idxBook[lastNode]][0]
        y, node = nodeinfo[i][0], nodeinfo[i][2]
        if y == lasty:
            nodes[level].append(node)
        else:
            nodes.append([node])
            level += 1
        nodeinfo[idxBook[node]][3] = level
    getChild(root, lBound, rBound, tree, nodeinfo, nodes, idxBook)
    getPreorder(tree, root)
    getPostorder(tree, root)
    return [result1, result2]


def getChild(node, lBound, rBound, tree, nodeinfo, nodes, idxBook):
    nIdx = idxBook[node]
    lvl = nodeinfo[nIdx][3]
    x = nodeinfo[nIdx][1]
    if lvl == len(nodes) - 1: # 자식 없는거 확정
        return
    for nxtNode in nodes[lvl + 1]:
        nxtIdx = idxBook[nxtNode]
        nx = nodeinfo[nxtIdx][1]
        if lBound <= nx <= rBound:
            if nx < x: # left
                tree[node][0] = nxtNode
                getChild(nxtNode, lBound, x - 1, tree, nodeinfo, nodes, idxBook)
            if nx > x: # right:
                tree[node][1] = nxtNode
                getChild(nxtNode, x + 1, rBound, tree, nodeinfo, nodes, idxBook)



def getPreorder(tree, node):
    global result1
    lChild, rChild = tree[node][0], tree[node][1]
    result1.append(node)
    if lChild != None:
        getPreorder(tree, lChild)
    if rChild != None:
        getPreorder(tree, rChild)


def getPostorder(tree, node):
    global result2
    lChild, rChild = tree[node][0], tree[node][1]
    if lChild != None:
        getPostorder(tree, lChild)
    if rChild != None:
        getPostorder(tree, rChild)
    result2.append(node)
