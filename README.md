# Route-Calculator
This project seeks to apply various algorithms to optimize travel paths between start and end locations. I used Rice University as the test map for this project and translated physical locations into a mathematical graph of nodes and edges.

### What algorithms are used in this project?
I implemented three main algorithms within this project.

The first is a BFS_DFS algorithm that can performed either Breadth-First Search (BFS) or Depth-First Search (DFS) depending on what Restricted-Access Container (RAC) is passed in as an input. If a Queue is passed in, BFS is performed; conversly, if a Stack is passed in, DFS is performed. This is an exercise in abstraction and encapsulation, allowing one function to have a wider range of applications.

The second algorithm is a recursive implementation of DFS. This implementation is intended to demonstrate the relative performance of DFS with an explicit stack data structure, as is the case with the BFS_DFS algorithm, versus an implicit stack, that being the Python call stack. 

Finally, the third algorithm is A*. A* searches based on actual distances between nodes as well as heuristic distances. Unsurprisingly, this performed the best out of the three algorithms.

In all, this project is a good demonstration of data structures and algorithms in a realistic application.

### What is the relative effectiveness of this project?
As seen in the video below, the GUI visually compares what Google Maps would suggest as the optimal route with the results of the selected algorithm. Using the buttons on the left side, a user can select a start node, end node, and which of the algorithms to test on the map of Rice University and its surrounding landmarks.


### Project Demo
In the video, the green and red markers indicate the start and end nodes, respectively. Orange edges mark paths to traversed nodes, whereas the green line denotes the final "optimized" route.

https://user-images.githubusercontent.com/84203383/146257840-06b6e782-8875-453e-8359-3489e5959861.mov

