# this is going to be the main file where I attempt to create a program that visualizes the shortest path
# between any two points in a 2d grid. In this sense, path is reffering to the number of intermediary squares between a start and 
# an end square.


#broad picture
#1. create graphics pannel where you can select 2 points 
#2. implement a* to find the shortest path between 2 points 
#3. visualize the search pattern 


from graphics import * 

from node import * 

#priority queue 
from queue import PriorityQueue

class ShortestPath:
    #width of window (in px), height, width of square, height of square
    def __init__(self, w, h, sqw, sqh):
        self.width = w
        self.height = h
        self.sqw = sqw
        self.sqh = sqh

    def distanceformula(self, node1, node2):
        return ((node1.getX() - node2.getX())**2 + (node1.getY() - node2.getY())**2)**.5

    def drawGrid(self):
        win = GraphWin(width = self.width, height = self.height) # create a window
        # create a window with self.width/self.sqw * self.height/self.sqh square units
        win.setCoords(0, 0, self.width/self.sqw, self.height/self.sqh) # set the coordinates of the window; bottom left is (0, 0) and top right is (10, 10)
        i = 0
        j = 0
        #draw grid
        for i in range(int(self.width/self.sqw)):
            for j in range(int(self.height/self.sqh)):
                square = Rectangle(Point(i,j), Point(i+1, j+1))
                square.draw(win)

        # prompt user to essentially pick a starting and ending point 
        print("Please pick a starting square and press any key once finished")
        point1 = win.getMouse() # record mouse press coords
        print(point1.getX, point1.getY)
        #i = x, j = y
        i1,j1 = int(point1.getX()), int(point1.getY())
        print(i,j)
        #color the start square
        start =  Rectangle(Point(i1,j1), Point(i1+1,j1+1))
        start.setFill('red')
        start.draw(win)

        # pick ending pt 
        print("Please pick a ending square and press any key once finished")
        point1 = win.getMouse() # record mouse press coords
        #i = x, j = y
        i2,j2 = int(point1.getX()), int(point1.getY())
        #color the ending square
        end =  Rectangle(Point(i2,j2), Point(i2+1,j2+1))
        end.setFill('red')
        end.draw(win)


      
        #initialize graph
        #SOME IMPORTANT NOTES:
        #all nodes are initialized with pixel values reffering to the bottom left corner of the square
        # the approximation I am using for distance to end node is simply the distance formula (i.e. sqrt(sqr(x2-x1) + sqr(y2-y1)))
        # (i.e. the absolute smallest distance from a current node to the end node)
        #visited nodes: this will be just an array... I need to check if the end node is in this list every time...expensive operation... could solve with a set but...
        #also once the program is running and you have selected both points, simply click once again to view the shortest path 
        
        visited = []

        #nodes to visit
        #making toVisit a priority queue, so we can select smallest path 
        #priority queues in py need to be sent a tuple with the first val of tuple being the priority
        toVisit = PriorityQueue()
        
        start = Node(i1,j1,True, False, None)
        end = Node(i2,j2, False, True, None)

        #set the values for start and end... distance formula to end node
        distanceToEnd = self.distanceformula(start,end)
        start.setCost(0, distanceToEnd)
       
        #add start node to the list of nodes that need to be visited
        totalCost = start.getTotalCost()
        toVisit.put((totalCost, start))
    
        #I need to check whether the end node is inside of the visited array 
        endInside = False
        for k in visited:
            if(k.isEnd()):
                endInside = True

        while((not(endInside)) and (not toVisit.qsize == 0)):
            #remeber coords are refering to bottom left corner
            #get smallest item in pq (based on total size) 
            currnode = toVisit.get()[1]
            i = currnode.getX()
            j = currnode.getY()
            
            #add some animation to the current node 
            x =  Rectangle(Point(i,j), Point(i+1,j+1))
            x.setFill("yellow")
            x.draw(win)

            #looping var 
            x = i - 1

            #make sure the current node has not been visited already
            checkNode = False
            for n in visited:
                if(n == currnode):
                    checkNode = True

            if(not checkNode):
                #traverse all of the squares immediatley neighboring the current square
                while x <= i + 1:
                    #y needs to be reset each time
                    y = j - 1
                    while y <= j + 1:
                        #first make sure they are within the scope of the screen # and make sure we are not adding the orignial node again
                        if((x >= 0 and x < self.width/self.sqw ) and (y >= 0 and y < self.height/self.sqh) and not (x == i and y == j)):
                            #check if the coords are that of the end
                            if(x == end.getX() and y == end.getY()):
                                #add the end node to visited
                                neighbor = Node(x, y, False, True, currnode)
                                visited.append(end)
                                #set our ref end equal to end so we can back trace
                                end = neighbor
                                #draw the end rectangle
                                current = Rectangle(Point(x,y), Point(x+1,y+1))
                                current.setFill("blue")
                                current.draw(win)
                                win.getMouse()
                                #set the loop condition to True, thus stopping the loop
                                endInside = True
                            #if it is not the end node
                            neighbor = Node(x, y, False, False, currnode)
                            #set distance from start node, distance from end node
                            #here we can safely say that all of node x's neighbors are 1 distance away from x 
                            neighbor.setCost(currnode.getStartCost() + 1, self.distanceformula(neighbor, end))
                            #add all of the neighboring nodes to the toVisit pq
                            toVisit.put((neighbor.getTotalCost(), neighbor))
                            #add some animations here - color the visited square pink 
                            current = Rectangle(Point(x,y), Point(x+1,y+1))
                            current.setFill("pink")
                            current.draw(win)
                    
                        y += 1
                    x += 1
                #add current node to visited
                visited.append(currnode)
        
        #now that shortest path to end has been found, back track and highlight the squares along the path 
        temp2 = end
        current = Rectangle(Point(temp2.getX(), temp2.getY()), Point(temp2.getX() + 1, temp2.getY() + 1))
        current.setFill("blue")
        current.draw(win)
        while(not temp2.getPreviousNode() == None):
            temp2 = temp2.getPreviousNode()
            current = Rectangle(Point(temp2.getX(), temp2.getY()), Point(temp2.getX() + 1, temp2.getY() + 1))
            current.setFill("blue")
            current.draw(win)
       
        win.getMouse()

#driver code -- feel free to change the size of the grid; again the grid is 1000px * 1000px with each square taking 10px
x = ShortestPath(1000,1000,10,10)
x.drawGrid()
