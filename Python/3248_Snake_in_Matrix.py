class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        map = {
            'UP'    : [-1, 0],
            'DOWN'  : [1, 0],
            'RIGHT' : [0, 1],
            'LEFT'  : [0, -1]
        }

        pos = [0, 0]
        for s in commands:
            pos[0] += map[s][0]
            pos[1] += map[s][1]
        
        return (pos[0] * n) + pos[1]
