def diagonalSort(mat):
    m, n = len(mat), len(mat[0])

    for r in range(m):
        d = []
        i, j = r, 0
        while i < m and j < n:
            d.append(mat[i][j]); i += 1; j += 1
        d.sort()

        i, j = r, 0
        for x in d:
            mat[i][j] = x; i += 1; j += 1

    for c in range(1, n):
        d = []
        i, j = 0, c
        while i < m and j < n:
            d.append(mat[i][j]); i += 1; j += 1
        d.sort()

        i, j = 0, c
        for x in d:
            mat[i][j] = x; i += 1; j += 1

    return mat

if __name__ == '__main__':
    m, n = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(m)]
    print(diagonalSort(mat))
