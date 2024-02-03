from searchAgent import SearchAgent, Rubiks2x2SearchProblem, rubiks2x2heuristic
from search import dfs

if __name__ == '__main__':
    scrambledState = (('w', 'w', 'w', 'w'), ('r', 'r', 'b', 'b'), ('g', 'g', 'r', 'r'), ('b', 'b', 'o', 'o'), ('o', 'o', 'g', 'g'), ('y', 'y', 'y', 'y'))
    searchAgent = SearchAgent(dfs, Rubiks2x2SearchProblem, rubiks2x2heuristic)
    searchAgent.registerInitialState(scrambledState)
    actions = searchAgent.getActions()
    print(actions)