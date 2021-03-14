class node():
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

def depth(tree):
    if tree==None:
        return 0
    else:
        left,right=depth(tree.left),depth(tree.right)
        return max(left,right)+1

def pre_order(tree):
    if tree==None:
        return
    else:
        print(tree.data)
        pre_order(tree.left)
        pre_order(tree.right)

if __name__=='__main__':
    tree=node('A',node('B',node('D'),node('E')),node('C'))
    print(depth(tree))
    print(pre_order(tree))

            