#Tasks
def diagonalDifference(arr):
        
        n = len(arr)
        a = sum(arr[i][i] for i in range(n))
        b = sum(arr[i][n-1-i] for i in range(n))
        return abs(a - b)

if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    print(result)

