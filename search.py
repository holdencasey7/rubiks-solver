from util import PriorityQueue

def dfs(problem):
    startState = problem.getStartState()
    if problem.isGoalState(startState):
        return []
    
    startNode = (startState, None, 0)
    frontier = PriorityQueue()
    frontier.push(startNode, startNode[2])
    reached = {startState: (startNode, None)}
    path = []

    while not frontier.isEmpty():
        node = frontier.pop()
        state = node[0]

        if problem.isGoalState(state):
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
            childState = childNode[0]
            newNode = (childNode[0], childNode[1], childNode[2] + node[2])
            if (not (childState in reached)) or newNode[2] < ((reached[childState])[0])[2]:
                reached.update({childState: (newNode, node)})
                frontier.push(newNode, newNode[2])

    # On failure return empty list?
    return []

def astar(problem, heuristic):
    return