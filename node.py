
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
        self.isEnd = False 
        self.prevNode = prevNode

    def addNeighbor(self,node):
        self.neighbor_list.append(node)
    
    def setCost(self,sc, ec):
        self.startcost, self.endcost = sc, ec
        self.totalcost = sc + ec

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