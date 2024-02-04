from searchAgent import SearchAgent, Rubiks2x2SearchProblem, rubiks2x2FacesHeuristic
from search import astar

if __name__ == '__main__':
    print("Using A* Search:")
    print("For faces, input lowercase first letter of color in order TL TR BL BR (reading order)")
    upFace = tuple(list(input("Up Face: ")))
    frontFace = tuple(list(input("Front Face: ")))
    leftFace = tuple(list(input("left Face: ")))
    rightFace = tuple(list(input("right Face: ")))
    backFace = tuple(list(input("back Face: ")))
    downFace = tuple(list(input("down Face: ")))

    scrambledState = (upFace, frontFace, leftFace, rightFace, backFace, downFace)
    searchAgent = SearchAgent(astar, Rubiks2x2SearchProblem, rubiks2x2FacesHeuristic)
    searchAgent.registerInitialState(scrambledState)
    actions = searchAgent.getActions()
    print(actions)