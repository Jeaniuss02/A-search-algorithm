import hwu_search

class State:
    def __init__(self, value, goal=False):
        self.x, self.y = value
        self.goal = goal

    def isGoal(self):
        return self.goal

    def getHeuristic(self, goal):
        return abs(self.x - goal.value.x) + abs(self.y - goal.value.y)
    
    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

def addChild(child, parent, color = "white"):
    if color == "grey":
        cost = 3
    else:
        cost = 1
    parent.addChild(child, cost)
    return child

class SearchOrder:    
    def addToFringe(self, frontier, parent, children):
        for child in children:
            gn = parent.gValue + child.cost #calculate the cost 
            hn = child.node.value.getHeuristic(goal) #calculate the heuristic
            fn = gn + hn #sum of cost and heuristic
            
            fringe_node = hwu_search.FringeNode(child.node, parent, child.cost)
            fringe_node.fval = fn
            frontier.append(fringe_node)
            
        frontier.sort(key=lambda node: node.fval) #sorting out the frontier with the f(n)

# First grid A: create 4x6 grid
# Define start state and goal state
start = hwu_search.Node(State((0, 0)))
goal = hwu_search.Node(State((3, 4), True))

# First grid A: create the first row of the grid
gridA01 = hwu_search.Node(State((0, 1)))
gridA02 = hwu_search.Node(State((0, 2)))
gridA03 = hwu_search.Node(State((0, 3)))
gridA04 = hwu_search.Node(State((0, 4)))
gridA05 = hwu_search.Node(State((0, 5)))

# First grid A: create the second row of the grid
gridA10 = hwu_search.Node(State((1, 0)))
gridA11 = hwu_search.Node(State((1, 1)))
gridA13 = hwu_search.Node(State((1, 3)))
gridA14 = hwu_search.Node(State((1, 4)))
gridA15 = hwu_search.Node(State((1, 5)))

# First grid A: create the third row of the grid
gridA20 = hwu_search.Node(State((2, 0)))
gridA21 = hwu_search.Node(State((2, 1)))
gridA22 = hwu_search.Node(State((2, 2)))
gridA24 = hwu_search.Node(State((2, 4)))
gridA25 = hwu_search.Node(State((2, 5)))

# First grid A: create the forth row of the grid
gridA30 = hwu_search.Node(State((3, 0)))
gridA31 = hwu_search.Node(State((3, 1)))
gridA32 = hwu_search.Node(State((3, 2)))
gridA35 = hwu_search.Node(State((3, 5)))

# Create nodes for each state and connect them
addChild(gridA01, start, "grey")
addChild(gridA10, start)
addChild(start, gridA10)
addChild(gridA11, gridA10, "grey")
addChild(gridA20, gridA10)
addChild(gridA10, gridA20)
addChild(gridA21, gridA20)
addChild(gridA30, gridA20)
addChild(gridA20, gridA30)
addChild(gridA31, gridA30)
addChild(start, gridA01)
addChild(gridA02, gridA01)
addChild(gridA11, gridA01, "grey")
addChild(gridA01, gridA11, "grey")
addChild(gridA10, gridA11)
addChild(gridA21, gridA11)
addChild(gridA11, gridA21, "grey")
addChild(gridA20, gridA21)
addChild(gridA22, gridA21, "grey")
addChild(gridA31, gridA21)
addChild(gridA21, gridA31)
addChild(gridA30, gridA31)
addChild(gridA32, gridA31)
addChild(gridA01, gridA02, "grey")
addChild(gridA03, gridA02)
addChild(gridA21, gridA22)
addChild(gridA32, gridA22)
addChild(gridA22, gridA32, "grey")
addChild(gridA31, gridA32)
addChild(gridA02, gridA03)
addChild(gridA04, gridA03)
addChild(gridA13, gridA03)
addChild(gridA03, gridA13)
addChild(gridA14, gridA13, "grey")
addChild(gridA03, gridA04)
addChild(gridA05, gridA04)
addChild(gridA14, gridA04, "grey")
addChild(gridA04, gridA14)
addChild(gridA13, gridA14)
addChild(gridA15, gridA14)
addChild(gridA24, gridA14, "grey")
addChild(gridA14, gridA24, "grey")
addChild(gridA25, gridA24)
addChild(goal, gridA24)
addChild(gridA04, gridA05)
addChild(gridA15, gridA05)
addChild(gridA05, gridA15)
addChild(gridA14, gridA15, "grey")
addChild(gridA25, gridA15)
addChild(gridA15, gridA25)
addChild(gridA24, gridA25, "grey")
addChild(gridA35, gridA25)
addChild(gridA25, gridA35)
addChild(goal, gridA35)

# Second grid: create 5x5 grid
# Define start state and goal state
start = hwu_search.Node(State((0, 0)))
goal = hwu_search.Node(State((4, 4), True))

# First grid B: create the first column of the grid
gridB10 = hwu_search.Node(State((1, 0)))
gridB20 = hwu_search.Node(State((2, 0)))
gridB40 = hwu_search.Node(State((4, 0)))


# First grid B: create the second column of the grid
gridB01 = hwu_search.Node(State((0, 1)))
gridB21 = hwu_search.Node(State((2, 1)))
gridB31 = hwu_search.Node(State((3, 1)))
gridB41 = hwu_search.Node(State((4, 1)))

# First grid B: create the third column of the grid
gridB02 = hwu_search.Node(State((0, 2)))
gridB32 = hwu_search.Node(State((3, 2)))
gridB42 = hwu_search.Node(State((4, 2)))

# First grid B: create the forth column of the grid
gridB03 = hwu_search.Node(State((0, 3)))
gridB23 = hwu_search.Node(State((2, 3)))
gridB33 = hwu_search.Node(State((3, 3)))
gridB43 = hwu_search.Node(State((4, 3)))

# First grid B: create the fifth column of the grid
gridB04 = hwu_search.Node(State((0, 4)))
gridB14 = hwu_search.Node(State((1, 4)))
gridB24 = hwu_search.Node(State((2, 4)))
gridB34 = hwu_search.Node(State((3, 4)))

# Create nodes for each state and connect them
addChild(gridB01, start)
addChild(gridB10, start, "grey")
addChild(start, gridB10)
addChild(gridB20, gridB10)
addChild(gridB10, gridB20, "grey")
addChild(gridB21, gridB20)
addChild(gridB41, gridB40)
addChild(start, gridB01)
addChild(gridB02, gridB01)
addChild(gridB20, gridB21)
addChild(gridB31, gridB21)
addChild(gridB21, gridB31)
addChild(gridB32, gridB31, "grey")
addChild(gridB41, gridB31)
addChild(gridB31, gridB41)
addChild(gridB40, gridB41)
addChild(gridB42, gridB41)
addChild(gridB01, gridB02)
addChild(gridB03, gridB02)
addChild(gridB31, gridB32)
addChild(gridB33, gridB32)
addChild(gridB42, gridB32)
addChild(gridB32, gridB42, "grey")
addChild(gridB41, gridB42)
addChild(gridB43, gridB42)
addChild(gridB02, gridB03)
addChild(gridB04, gridB03)
addChild(gridB24, gridB23)
addChild(gridB33, gridB23)
addChild(gridB23, gridB33)
addChild(gridB32, gridB33, "grey")
addChild(gridB34, gridB33, "grey")
addChild(gridB43, gridB33)
addChild(gridB33, gridB43)
addChild(gridB42, gridB43)
addChild(start, gridB43)
addChild(gridB03, gridB04)
addChild(gridB14, gridB04, "grey")
addChild(gridB04, gridB14)
addChild(gridB24, gridB14)
addChild(gridB14, gridB24, "grey")
addChild(gridB23, gridB24)
addChild(gridB34, gridB24, "grey")
addChild(gridB24, gridB34)
addChild(gridB33, gridB34)
addChild(goal, gridB34)

# Create a search problem instance and perform the search
order = SearchOrder()
problem = hwu_search.SearchProblem(order)
problem.doSearch(start)
