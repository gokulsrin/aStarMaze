# this is going to be the main file for the maze thing that I attempt to create


#broad picture
#1. create graphics pannel where you can select 2 points 
#2. implement a* to find the shortest path between 2 points 
#3. visualize the search pattern 
#4. allow for the addition of obstacles

from graphics import * 

from node import * 

#priority queue 
from queue import PriorityQueue

class ShortestPath:
    def __init__(self, w, h, sqw, sqh):
        self.width = w
        self.height = h
        self.sqw = sqw
        self.sqh = sqh

    def distanceformula(self, node1, node2):
        return ((node1.getX() - node2.getX())**2 + (node1.getY() - node2.getY())**2)**.5

    def drawGrid(self):
        win = GraphWin(width = self.width, height = self.height) # create a window
        # create a window with 80*80 square units
        win.setCoords(0, 0, self.width/self.sqw, self.height/self.sqh) # set the coordinates of the window; bottom left is (0, 0) and top right is (10, 10)
        i = 0
        j = 0
        #draw 80 * 80 grid
        for i in range(int(self.width/self.sqw)):
            for j in range(int(self.height/self.sqh)):
                square = Rectangle(Point(i,j), Point(i+1, j+1))
                square.draw(win)

        # prompt user to essentially pick a starting and ending point 
        print("Please pick a starting square and press any key once finished")
        point1 = win.getMouse() # pause before closing
        print(point1.getX, point1.getY)
        #i = x, j = y
        i,j = int(point1.getX()), int(point1.getY())
        print(i,j)
        start =  Rectangle(Point(i,j), Point(i+1,j+1))
        start.setFill('red')
        start.draw(win)

        # pick ending pt 
        print("Please pick a ending square and press any key once finished")
        point1 = win.getMouse() # pause before closing
        #i = x, j = y
        i,j = int(point1.getX()), int(point1.getY())
        end =  Rectangle(Point(i,j), Point(i+1,j+1))
        end.setFill('red')
        end.draw(win)

        #operate like top left starting bottom right ending
        #initialize graph
        #all nodes are initialized with values being the bottom left corner of the square

        # the approximation I am using for distance to end node is simply the distance formula 
        # (i.e. the absolute smallest distance from a current node to the end node)

        #visited nodes: this will be a set, and we simply need to check if something has been visited using .contains 
        visited = set([])

        #nodes to visit
        #making toVisit a priority queue, so we can select smallest path 
        toVisit = PriorityQueue()
        
        start = Node(0,4,True, False, None)
        end = Node(4,0, False, True, None)
        #set the values for start and end... distance formula to end node
        distanceToEnd = self.distanceformula(start,end)
        start.setCost(0, distanceToEnd)
       

        #add start node to the list of nodes that need to be visited
        totalCost = start.getTotalCost()
        toVisit.put(totalCost, start)

        #testing
        print(distanceToEnd)
        print(toVisit)

        o = toVisit.get()
        print(o)

        #use heap instead and you will solve problem
        #essentially while the end node has not been visited
        while(not(end in visited) and not toVisit.empty):
            print("hello")
            #remeber coords are refering to bottom left corner
            #get smallest item in pq (based on total size) 
            currnode = toVisit.get()
            i = currnode.getX()
            j = currnode.getY()
            
            #add some animation to the current node 
            x =  Rectangle(Point(i,j), Point(i+1,j+1))
            x.setFill("yellow")
            x.draw(win)

            #traverse around the node
            x = i - 1
            y = j - 1
            while x <= i + 1:
                while y <= j + 1:
                    #first make sure they are within the scope of the screen 
                    if((x >= 0 and x < self.width/self.sqw ) and (y >= 0 and y < self.height/self.sqh)):
                        #make sure these are not corners 
                        if(not(abs(x/y) == 1)):
                            #visit the 4 nodes (top, left, right, and bottom around the node and calculate the distance values from the previous node
                            neighbor = Node(x, y, False, False, currnode)
                            #set distance from start node, distance from end node
                            #here we can safely say that all of node x's neighbors are 1 distance away from x 
                            neighbor.setCost(currnode.getStartCost() + 1, self.distanceformula(neighbor, end))
                            #add all of the neighboring nodes to the toVisit pq
                            toVisit.put((neighbor.getTotalCost, neighbor))

                            #add some animations here - color the visited square pink 
                            current = Rectangle(Point(x,y), Point(x+1,y+1))
                            current.setFill("pink")
                            current.draw(win)

                            #testing 
                            print("coords: "+ x,y)


            #add current node to visited
            visited.add(currnode)

        win.getMouse()

x = ShortestPath(50,50,10,10)
x.drawGrid()