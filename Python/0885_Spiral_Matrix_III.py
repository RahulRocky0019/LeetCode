class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        result = []
        action = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        idx = 0
        step = 1

        while len(result) < rows * cols:
            for _ in range(2):
                for _ in range(step): 
                    if 0 <= rStart < rows and 0 <= cStart < cols:
                        result.append([rStart, cStart])

                    rStart += action[idx][0]
                    cStart += action[idx][1]
                idx = (idx + 1) % 4
            step += 1

        return result
