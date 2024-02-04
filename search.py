from util import PriorityQueue, Stack, Queue

def ucs(problem):
    #print("***DEBUG***: Starting DFS")
    startState = problem.getStartState()
    #print("***DEBUG***: DFS Initial State: ", startState)
    if problem.isGoalState(startState):
        return []
    #print("***DEBUG***: Goal Check Complete")

    startNode = (startState, None, 0)
    frontier = PriorityQueue()
    frontier.push(startNode, startNode[2])
    reached = {startState: (startNode, None)}
    path = []

    while not frontier.isEmpty():
        node = frontier.pop()
        state = node[0]

        if problem.isGoalState(state):
            #print("***DEBUG***: Goal State Identified", state)
            # Add how we got here
            path.append(node[1])
            # Add how we got to parent nodes
            parentNode = (reached[state])[1]
            while parentNode[1] is not None:
                path.append(parentNode[1])
                parentNode = (reached[parentNode[0]])[1]
            path.reverse()
            return path

        for childNode in problem.getSuccessors(state):
            #print("***DEBUG***: Child Node Found")
            childState = childNode[0]
            newNode = (childNode[0], childNode[1], childNode[2] + node[2])
            if (not (childState in reached)) or newNode[2] < ((reached[childState])[0])[2]:
                reached.update({childState: (newNode, node)})
                frontier.push(newNode, newNode[2])

    # On failure return empty list?
    return []

def dfs(problem):
    startState = problem.getStartState()
    if problem.isGoalState(startState):
        return []
    
    startNode = (startState, None, None)
    startPathedNode = (startNode, list())
    frontier = Stack()
    frontier.push(startPathedNode)
    reached = {startState}

    while not frontier.isEmpty():
        pathedNode = frontier.pop()
        node, actionList = pathedNode
        state = node[0]
        reached.add(state)
        if problem.isGoalState(state):
            return actionList

        for childNode in problem.getSuccessors(state):
            childState = childNode[0]
            if not childState in reached:
                currentActionsPlusNewAction = actionList + [childNode[1]]
                childPathedNode = (childNode,currentActionsPlusNewAction)
                frontier.push(childPathedNode)
            
    return []

def astar(problem, heuristic):
    startState = problem.getStartState()
    if problem.isGoalState(startState):
        return []
    
    startNode = (startState, None, 0)
    frontier = PriorityQueue()
    frontier.push(startNode, startNode[2] + heuristic(startState, problem))
    reached = {startState: (startNode, None)}
    path = []

    while not frontier.isEmpty():
        node = frontier.pop()
        state = node[0]

        if problem.isGoalState(state):
            path.append(node[1])
            parentNode = (reached[state])[1]
            while parentNode[1] is not None:
                path.append(parentNode[1])
                parentNode = (reached[parentNode[0]])[1]
            path.reverse()
            return path


        for childNode in problem.getSuccessors(state):
            childState = childNode[0]
            newNode = (childNode[0], childNode[1], childNode[2] + node[2])
            currCost = newNode[2]
            currHeuristic = heuristic(childState, problem)
            totalCost = currCost + currHeuristic
            if (not (childState in reached)) or currCost < ((reached[childState])[0])[2]:
                reached.update({childState: (newNode, node)})
                frontier.push(newNode, totalCost)

    return []


def bfs(problem):
    startState = problem.getStartState()
    if problem.isGoalState(startState):
        return []

    startNode = (startState, None, None)
    frontier = Queue()
    frontier.push(startNode)
    reached = {startState: None}
    path = []

    while not frontier.isEmpty():
        # Get the 'least deep' node
        node = frontier.pop()
        state = node[0]

        if problem.isGoalState(state):
                # First add how we got to the goal state
                path.append(node[1])

                # Add how we got to each parent
                parentNode = reached[state]
                while parentNode[1] is not None:
                    path.append(parentNode[1])
                    parentNode = reached[parentNode[0]]

                path.reverse()
                return path

        # Iterate over children
        for childNode in problem.getSuccessors(state):
            childState = childNode[0]
            
            # Remember how the child node was reached
            if not (childState in reached):
                reached.update({childState : node})
                frontier.push(childNode)
            
    # On failure, return empty list?
    return []