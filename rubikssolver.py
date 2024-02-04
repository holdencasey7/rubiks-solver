from searchAgent import SearchAgent, Rubiks2x2SearchProblem, rubiks2x2heuristic
from search import dfs, bfs, astar, ucs

if __name__ == '__main__':
    scrambledState = (('w', 'w', 'r', 'g'), ('g', 'o', 'r', 'o'), ('g', 'w', 'r', 'g'), ('y', 'b', 'y', 'b'), ('o', 'o', 'r', 'y'), ('y', 'b', 'b', 'w'))
    searchAgent = SearchAgent(astar, Rubiks2x2SearchProblem, rubiks2x2heuristic)
    searchAgent.registerInitialState(scrambledState)
    actions = searchAgent.getActions()
    print(actions)