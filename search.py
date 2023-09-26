# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    stack = util.Stack()
    stack.push((problem.getStartState(), []))

    explored = set()

    while not stack.isEmpty():
        currentState, actions = stack.pop()

        # If this currentState is Goal state return its actions.
        if problem.isGoalState(currentState):
            return actions

        # Marking the state as explored
        explored.add(currentState)

        # Get the successors of the current state
        for nextState, action, _ in problem.getSuccessors(currentState):
            if nextState not in explored:
                # Append the action to reach the next state to the current actions list
                newActions = actions + [action]
                stack.push((nextState, newActions))

        # If the goal state isn't reached, return an empty list
    return []

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    queue = util.Queue()
    queue.push((problem.getStartState(), []))

    explored = set()
    explored.add(problem.getStartState())

    while not queue.isEmpty():
        currentState, actions = queue.pop()


        # If this currentState is Goal state return its actions.
        if problem.isGoalState(currentState):
            return actions

        # Get the successors of the current state
        for nextState, action, _ in problem.getSuccessors(currentState):
            if nextState not in explored:
                # Append the action to reach the next state to the current actions list
                newActions = actions + [action]
                queue.push((nextState, newActions))
                explored.add(nextState)

        # If the goal state isn't reached, return an empty list
    return []


def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    priorityqueue = util.PriorityQueue()

    # Initialize the queue with start state and cost 0
    priorityqueue.push((problem.getStartState(), []), 0)

    # This is meant to take unique elements like graph
    explored = set()

    while not priorityqueue.isEmpty():
        currentState, actions = priorityqueue.pop()

        # If this currentState is Goal state return its actions.
        if problem.isGoalState(currentState):
            return actions

        if currentState not in explored:
            explored.add(currentState)
            for nextState, action, cost in problem.getSuccessors(currentState):
                if nextState not in explored:
                    newActions = actions + [action]
                    # Calculate the total cost for newActions
                    totalCost = problem.getCostOfActions(newActions)
                    priorityqueue.push((nextState, newActions), totalCost)

    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    priorityqueue = util.PriorityQueue()

    # Start state with cost as heuristic value only because actual cost to start is 0
    startState = problem.getStartState()
    priorityqueue.push((startState, []), heuristic(startState, problem))

    explored = set()

    while not priorityqueue.isEmpty():
        currentState, actions = priorityqueue.pop()

        # If this currentState is Goal state return its actions.
        if problem.isGoalState(currentState):
            return actions

        if currentState not in explored:
            explored.add(currentState)
            for nextState, action, cost in problem.getSuccessors(currentState):
                if nextState not in explored:
                    newActions = actions + [action]
                    # Calculate the total cost for newActions which is actual cost + heuristic
                    totalCost = problem.getCostOfActions(newActions) + heuristic(nextState, problem)
                    priorityqueue.push((nextState, newActions), totalCost)

    return []
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
