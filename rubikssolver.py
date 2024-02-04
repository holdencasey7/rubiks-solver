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
    scrambledState = (('y', 'b', 'r', 'o'), ('y', 'g', 'w', 'w'), ('b', 'g', 'r', 'g'), ('w', 'r', 'o', 'o'), ('y', 'o', 'g', 'b'), ('r', 'b', 'w', 'y'))
    searchAgent = SearchAgent(searchFunc, Rubiks2x2SearchProblem, rubiks2x2FacesHeuristic)
    searchAgent.registerInitialState(scrambledState)
    actions = searchAgent.getActions()
    print(actions)