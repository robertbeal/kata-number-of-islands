# number of islands problem

Given a multi-dimensional array of 1's and 0's (1 = land, 0 = sea) find the number of islands.

I've mapped the problem into objects to make it easier to understand. It uses a queue (rather than my original recursive solution) to explore all neighbouring land. This allows me to choose whether to search breadth-first or depth-first and makes debugging simpler. I also track visited coordinates for efficiency (currently O(n)) (and so I don't explore already explored land).

