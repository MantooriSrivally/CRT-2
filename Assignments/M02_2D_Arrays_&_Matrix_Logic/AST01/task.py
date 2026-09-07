from typing import List

def spiralMatrixIII(rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
    
    ans = [[rStart, cStart]]
    r, c = rStart, cStart
    d = [(0,1),(1,0),(0,-1),(-1,0)]
    step = 1

    while len(ans) < rows * cols:
        for i in range(4):
            for _ in range(step):
                r += d[i][0]
                c += d[i][1]
                if 0 <= r < rows and 0 <= c < cols:
                    ans.append([r, c])
            if i % 2 == 1:
                step += 1

    return ans


if __name__ == '__main__':
   rows,cols,rStart,cStart = map(int,input().split())
   print(spiralMatrixIII(rows,cols,rStart,cStart))