'''arr = list(map(int,input().split()))
res = []
for i in arr:
    if i % 2 != 0:#odd 
        #if i%2 == 0
        res.remove(i)#res.append(i)

print(res)
'''
'''arr=list(map(int,input().split()))
i=0
for j in range(len(arr)):
    if arr[j] % 2 ==0:
        arr[i]=arr[j]
        i += 1
print(arr[:i])'''
#input:python
#output:nohtyp
s=input()
li=list(s)
left,right=0,len(s)-1
while left<right:
    li[left],li[right]=li[right],li[left]
    left += 1
    right -= 1
print("".join(li))