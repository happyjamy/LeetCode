from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        r = [0, 0, -1, 1]
        c = [-1, 1, 0, 0]
        check = [[True for i in range(len(grid[0]))] for z in range(len(grid))]


        def bfs(start,check):

            start_y,start_x = start

            q = deque()
            q.append(start)
            check[start_y][start_x] = False

            while q:
                y, x = q.popleft()
                grid[y][x] = '0'

                for i in range(4):
                    nex_y = y + r[i]
                    nex_x = x + c[i]
                    if 0 <= nex_y < len(grid) and 0 <= nex_x < len(grid[0]) and check[nex_y][nex_x] and grid[nex_y][nex_x] == '1':
                        q.append((nex_y, nex_x))
                        check[nex_y][nex_x] = False

        for i in range(len(grid)):
            for z in range(len(grid[0])):
                if grid[i][z] == '1':
                    cnt += 1
                    bfs((i, z),check)

        return cnt
                
        
                
        
                        
                
                
        
        
        