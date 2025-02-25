from typing import Tuple, List, Set

class MonkeyGameDFS:
    def __init__(self, monkey_start: Tuple[int, int], banana_pos: Tuple[int, int]):
        self.grid_size = 3  # 3x3 grid
        self.monkey_start = monkey_start
        self.banana_pos = banana_pos
        self.moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    def is_valid(self, x: int, y: int) -> bool:
        """Check if the move is within bounds."""
        return 0 <= x < self.grid_size and 0 <= y < self.grid_size

    def dfs(self, position: Tuple[int, int], visited: Set[Tuple[int, int]]) -> bool:
        """Perform DFS to find a path to the banana."""
        if position == self.banana_pos:
            return True  # Reached the banana 🎉

        visited.add(position)

        for dx, dy in self.moves:
            new_x, new_y = position[0] + dx, position[1] + dy
            if self.is_valid(new_x, new_y) and (new_x, new_y) not in visited:
                if self.dfs((new_x, new_y), visited):
                    return True  # Found a valid path

        return False  # No path found

    def can_reach_banana(self) -> bool:
        """Check if the monkey can reach the banana using DFS."""
        return self.dfs(self.monkey_start, set())

# Example Usage
game = MonkeyGameDFS((0, 0), (2, 2))  # Monkey at (0,0), Banana at (2,2)
print("Can the monkey reach the banana?", game.can_reach_banana())
