# number of islands problem

Given a multi-dimensional array of 1's and 0's (1 = land, 0 = sea) that represents a map, find the number of islands. An island is a collection of 1's that are adjacent to one another.

I've mapped the problem into domain objects to make it easier to understand. It uses a queue (rather than my original recursive solution) to explore all neighbouring land. This allows me to choose whether to search breadth-first or depth-first and makes debugging simpler. I also track visited coordinates for efficiency (not truly O(n) as I check if each coordinate has been visted rather than removing it from processing completely) so that coordinates aren't explored more than once.

