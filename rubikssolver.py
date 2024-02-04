from searchAgent import SearchAgent, Rubiks2x2SearchProblem, rubiks2x2FacesHeuristic
from search import dfs, bfs, astar, ucs
import sys

if __name__ == '__main__':
    _, search = sys.argv
    if search == 'dfs':
        searchFunc = dfs
    elif search == 'bfs':
        searchFunc = bfs
    elif search == 'astar':
        searchFunc = astar
    elif search == 'ucs':
        searchFunc = ucs
    else:
        print("Please enter search function as argument")
        sys.exit()
    
    print("Using Search:", search)
    print("For faces, input lowercase first letter of color in order TL TR BL BR (reading order)")
    upFace = tuple(list(input("Up Face: ")))
    frontFace = tuple(list(input("Front Face: ")))
    leftFace = tuple(list(input("left Face: ")))
    rightFace = tuple(list(input("right Face: ")))
    backFace = tuple(list(input("back Face: ")))
    downFace = tuple(list(input("down Face: ")))

    scrambledState = (upFace, frontFace, leftFace, rightFace, backFace, downFace)
    searchAgent = SearchAgent(searchFunc, Rubiks2x2SearchProblem, rubiks2x2FacesHeuristic)
    searchAgent.registerInitialState(scrambledState)
    actions = searchAgent.getActions()
    print(actions)