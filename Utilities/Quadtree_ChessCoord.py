"""Quadtree_ChessCoord.py"""
""" Quadtree special for chess coordinate system"""
""" depth 1 node 1 contains A5-D8"""
""" depth 2 node 1 contains (A,8) (B,8) (A,7) (B,7)"""

class QuadTreeNode:
    def __init__(self,x_min,y_min,max_depth,depth = 0):
        self.x_min = x_min
        self.y_min = y_min
        self.size = pow(2,max_depth-depth)
        self.depth = depth
        self.max_depth = max_depth
        self.children = []
        self.data = None 
    
    def insert(self,x,y):
        if self.depth == self.max_depth: 
            self.data = (x,y)
        if self.depth < self.max_depth:
            if self.children == []: 
                self.subdivide()
            for child in self.children:
                if x >= child.x_min and x < child.x_min + child.size and y >= child.y_min and y < child.y_min + child.size:
                    child.insert(x,y)
    # order rule: first consider y value, then x value. 
    # big y value first, then small x value
    # for example （A,8）(B,8) (A,7) (B,7)
    def subdivide(self):
        size = self.size // 2 
        x_min_ori = self.x_min
        y_min_ori = self.y_min
        x_min = self.x_min + size
        y_min = self.y_min + size
        self.children.append(QuadTreeNode(x_min_ori,y_min,self.max_depth,self.depth+1)) 
        self.children.append(QuadTreeNode(x_min,y_min,self.max_depth,self.depth+1)) 
        self.children.append(QuadTreeNode(x_min_ori,y_min_ori,self.max_depth,self.depth+1)) 
        self.children.append(QuadTreeNode(x_min,y_min_ori,self.max_depth,self.depth+1)) 
    def print_tree(self, indent=0):
        # print all nodes and the depth of the node
        print(' ' * indent + f'{self.data} depth: {self.depth}')
        for child in self.children:
            child.print_tree(indent + 2)
    # get the number of vibration 
    # it should be a list containing the index of the first child, 
    # index of the second child, index of the third child
    # for example: [1,1,1] refers to A8
    def find_element(self, x,y,output = None):
        if output is None:
            output = [-1, -1, -1]  
        for child in self.children:
            if child.data == (x,y):
                output[child.depth-1] = self.children.index(child)+1
                return output
            elif (x >= child.x_min and 
                  x < child.x_min + child.size and 
                  y >= child.y_min and 
                  y < child.y_min + child.size):
                    output[child.depth-1] = self.children.index(child)+1
                    result = child.find_element(x, y, output)
                    if result !=[-1, -1, -1]:     
                        return result
preset_tree = QuadTreeNode(1,1,3)  
# insert all coordinates
for x in range(9):
    for y in range(9):
        preset_tree.insert(x, y)
  
def find_coord(coord_str):
    letter = coord_str[0].lower()
    x = ord(letter) - ord('a')+1
    y = int(coord_str[1])
    return preset_tree.find_element(x,y) 
if __name__ == "__main__":
    print(preset_tree.find_element(8, 8))
    print(find_coord("a4"))