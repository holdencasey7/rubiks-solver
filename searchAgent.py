from twoxtwocube import Moves, Agent, Problem
from search import dfs, astar
import time

class SearchAgent(Agent):
    def __init__(self, search, problem, heuristic):
        if search == astar: # TODO: fix
            self.searchFunction = lambda x: search(x, heuristic)
        else:
            self.searchFunction = search
        
        self.problem = problem


    def registerInitialState(self, state):
        startTime = time.time()
        problem = self.problem(state)
        self.actions = self.searchFunction(problem) # Search function returns a list of actions
        totalCost = problem.getCostOfActions(self.actions)
        print('Path found with total cost of %d in %.1f seconds' % (totalCost, time.time() - startTime))
        print('Search nodes expanded: %d' % problem._expanded)

        
    def getActions(self):
        return self.actions
        

class Rubiks2x2SearchProblem(Problem):
    """
    State space is color combinatins on 2x2 rubiks cube
    """

    def __init__(self, scrambledState):
        self.startingState = scrambledState
        # self.upFace, self.frontFace, self.leftFace, self.rightFace, self.backFace, self.downFace = scrambledState
        self._expanded = 0

        """ 
        State format:
        ((w, w, w, w), (r, r, r, r), etc)
        Top left, top right, bottom left, bottom right
        U F L R B D
        """


    def getStartState(self):
        return self.startingState
    

    def isGoalState(self, state):
        allFacesSameColor = True
        for face in state:
            if face.count(face[0]) != len(face):
                allFacesSameColor = False
        return allFacesSameColor
    

    def getSuccessors(self, state):
        """
        Returns a list of nodes with the format
        ((next state), move to get there)
        """
        nextStateNodes = []
        for move in Moves.moves:
            cost = 1
            if move == Moves.tperm:
                cost = 15
            elif move == Moves.sune:
                cost = 8
            nextStateNodes.append((move(state), move, cost))
        self._expanded += 1
        return nextStateNodes
    

    def getCostOfActions(self, actions):
        if actions is None:
            return 9999
        
        totalCost = 0
        for action in actions:
            if action == Moves.tperm:
                totalCost += 15
            elif action == Moves.sune:
                totalCost += 8
            else:
                totalCost += 1
        return totalCost
    
### TODO: implement
def rubiks2x2heuristic(state, problem):
    return 0


