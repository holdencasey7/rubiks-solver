from twoxtwocube import Moves

class Rubiks2x2SearchProblem:
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
            nextStateNodes.append((move(state), move))
        self._expanded += 1
        return nextStateNodes
    

    def getCostOfActions(self, actions):
        if actions is None:
            return 9999
        
        totalCost = 0
        for action in actions:
            if action is Moves.tperm:
                totalCost += 15
            elif action is Moves.sune:
                totalCost += 8
            else:
                totalCost += 1
        return totalCost