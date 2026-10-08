def next_greater(arr):
    n=len(arr)
    res=[-1]*n
    stack=[]
    for i in range(n):
        while stack and arr[stack[-1]]<arr[i]:
            index=stack.pop()
            