# Route-Calculator
This project seeks to apply various algorithms to optimize travel paths between start and end locations. I used Rice University as the test map for this project and translated physical locations into a mathematical graph of nodes and edges.

### What algorithms are used in this project?
I implemented three main algorithms within this project.

The first is a BFS_DFS algorithm that can performed either Breadth-First Search (BFS) or Depth-First Search (DFS) depending on what Restricted-Access Container (RAC) is passed in as an input. If a Queue is passed in, BFS is performed; conversly, if a Stack is passed in, DFS is performed. This was an exercise in abstraction and encapsulation, allowing one function to have a wider range of applications.

The second algorithm was a recursive implementation of DFS. This implementation is intended to demonstrate the relative performance of DFS with an explicit stack data structure, as is the case with the BFS_DFS algorithm, versus an implicit stack, that being the Python call stack. 

Finally, the third algorithm is the A<sup>*</sup> algorithm. 
