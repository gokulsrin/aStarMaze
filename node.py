
#this is the class that contains the node for the a* search

# the node should contain the x,y coord of node 
# as well as the neighbors of the node

class Node:
    def __init__(self,x,y, isStart, isEnd, prevNode):
        self.x = x
        self.y = y 
        self.neighbor_list = []
        self.startcost = 0
        self.endcost = 0
        self.totalcost = 0
        self.isStart = False
        self.isEnd = isEnd
        self.prevNode = prevNode

    def addNeighbor(self,node):
        self.neighbor_list.append(node)
    
    def setCost(self,sc, ec):
        self.startcost, self.endcost = sc, ec
        self.totalcost = sc + ec

    def isEnd(self):
        return self.isEnd

    def getTotalCost(self):
        return self.totalcost
        
    def getStartCost(self):
        return self.startcost

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getPreviousNode(self):
        return self.prevNode
    def __str__(self):
        return "X:" + str(self.x) +"; Y:" + str(self.y) + "; Total Coast: " + str(self.totalcost)
    
    #not sure if the comparison is correct
    def __lt__(self,other) : 
             if self.totalcost < other.getTotalCost():
                   return True
    #defined equality between node objects (i.e. their coords have to match)
    def __eq__(self, other):
        if not other == None:
            return self.x == other.getX() and self.y == other.getY()
        else:
            return False
       