** Task-1: Vaccum cleaner problem: **

This problem involves designing two types of agents (Simple Reflex Agent and Table-Driven Agent) to clean multiple rooms in an environment.

Initial State:
All rooms start as dirty (['dirty', 'dirty', 'dirty', 'dirty']).
The agent begins in Room A (for Simple Reflex Agent).
Agent Behaviors:
Simple Reflex Agent:
Observes the current room.
Cleans it if dirty, then moves to the next room.
Continues until all rooms are clean.
Table-Driven Agent:
Uses a predefined lookup table to decide actions based on the current state of all rooms.
Cleans rooms according to the table’s rules.
Final State:
All rooms are clean (['clean', 'clean', 'clean', 'clean']).
The agent stops after completing its task.
Key Differences:
The Simple Reflex Agent makes dynamic decisions based on perception.
The Table-Driven Agent follows a static set of rules from a predefined table.
Conclusion
Both agents effectively clean the rooms, but the Simple Reflex Agent is more flexible, whereas the Table-Driven Agent is limited by its predefined table.


** Task-2: Water jug problem: **

Problem Statement

You have two jugs:

A 5-liter jug (Jug A)
A 3-liter jug (Jug B)
Your goal is to measure exactly 4 liters using these two jugs. You can perform the following operations:

Fill a jug completely.
Empty a jug completely.
Pour water from one jug to another until one is full or the other is empty.
Solution Approach
We solve this problem using a step-by-step approach where we follow valid operations until we reach exactly 4 liters in Jug A or Jug B.

Steps to Reach 4 Liters:

Fill Jug A (5-liter jug) completely. (5,0)
Pour water from Jug A → Jug B until Jug B is full. (2,3)
Empty Jug B. (2,0)
Pour water from Jug A → Jug B again. (0,2)
Fill Jug A completely again. (5,2)
Pour water from Jug A → Jug B until Jug B is full. (4,3)
Now, Jug A contains exactly 4 liters, which is the required target.



** Task-3: DFS and BFS: **

1. Depth First Search (DFS):

DFS explores a tree or graph deep before moving to the next branch.
Uses a stack (either explicitly or via recursion).
Types of DFS Traversals in Trees:
Preorder (Root → Left → Right)
Inorder (Left → Root → Right)
Postorder (Left → Right → Root)


2. Breadth First Search (BFS):

BFS explores all neighbors before moving deeper.
Uses a queue (FIFO order).
Also known as Level Order Traversal in trees.


** Task-4: Monkey Banana problem:

Monkey-Banana Problem (AI & Problem Solving)

Problem: A monkey is in a room where a banana is hanging from the ceiling, out of reach. A box is present in the room that the monkey can use to reach the banana.
Solution Approach:
Represent the problem as a state-space search.
Use state representation (monkey’s position, box position, banana status).
Apply search algorithms (DFS, BFS, A*, or rule-based AI) to find a sequence of actions:
Move to the box
Push the box under the banana
Climb the box
Grab the banana (goal state)


** Task-5: 8-puzzle problem:

8-Puzzle Problem (Search & Heuristic AI)

Problem: A 3×3 sliding puzzle with 8 numbered tiles and one empty space. The goal is to move the tiles to match a predefined configuration.
Solution Approach:
Represent the puzzle as a state-space with moves (left, right, up, down).
Use search algorithms:
Breadth-First Search (BFS) for the shortest solution.
Depth-First Search (DFS) for exhaustive search.
A Algorithm* with the Manhattan Distance heuristic for efficient solving.


** Task-6: Hangman game:

Hangman (Game & String Processing)

Problem: A word-guessing game where a player must guess letters of a hidden word within a limited number of attempts.
Solution Approach:
Store a dictionary of possible words.
Randomly select a word and hide it.
Process user input to check guessed letters:
If correct, reveal the letter(s) in the word.
If incorrect, reduce the remaining chances.
Win Condition: All letters guessed correctly.
Lose Condition: Exceed the maximum number of incorrect guesses.
AI Implementation: AI can play optimally by choosing the most frequent letters first (like ‘E’, ‘T’, ‘A’).


** task-7: 8-Queens problem:

8-Queens Problem (Backtracking AI)
Problem: Place 8 queens on a chessboard such that no two queens attack each other.
Solution Approach:
State Representation: Board as an array where index = row and value = column.
Constraints: No two queens in the same row, column, or diagonal.
Algorithm:
Backtracking: Place queens row by row, backtrack if constraints are violated.
Optimized Approaches: Genetic algorithms or CSP solvers.

