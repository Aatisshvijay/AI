4. Uniform Cost Search (UCS): Fuel-Efficient Routing
Narrative: Minimize fuel consumption for a long-haul flight by finding the most cost-effective route.

Solution Approach:

Algorithm: Uniform Cost Search (UCS) is used because it finds the least-cost path in a weighted graph.
State Space: Nodes represent airports, and edges represent possible flight paths with a cost function based on fuel consumption.
Cost Function:
Distance traveled
Wind patterns (tailwinds reduce fuel use, headwinds increase it)
Altitude effects on fuel burn
Implementation Steps:
Start from the departure airport.
Expand the least-cost node first (i.e., the airport with the lowest total fuel cost so far).
Continue until reaching the destination airport.

Backtrack to reconstruct the optimal path.
Challenges & Extensions:

Challenges:
Defining a realistic cost function balancing speed, fuel use, and wind patterns.
Handling real-time changes in air traffic or fuel prices.
Extensions:
Introducing penalties for exceeding time limits or entering restricted zones

![image](https://github.com/user-attachments/assets/326d9888-0c48-4cc5-bfd0-f8a7f41fbe72)

//output
![PHOTO-2025-03-03-11-35-05](https://github.com/user-attachments/assets/2a921820-cea6-4d3c-8ee7-c81c85f798b9)
