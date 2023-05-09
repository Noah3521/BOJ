import sys
input = sys.stdin.readline

result=[]
def mergeSort(A):
    global result
    if len(A)==1:
        return A
    mid=(len(A)+1)//2
    # print("A[:mid]",A[:mid])
    left=mergeSort(A[:mid])
    # print("A[mid:]",A[mid:])
    right=mergeSort(A[mid:])
    l=0
    r=0
    res=[]
    while l<len(left) and r<len(right):
        if left[l]<right[r]:
            res.append(left[l])
            result.append(left[l])
            # print("left",res, "left[l]", left[l], "l",l)
            l+=1
        else:
            res.append(right[r])
            result.append(right[r])
            # print("right",res, "right[r]",right[r], "r",r)
            r+=1
    while l < len(left):
        res.append(left[l])
        result.append(left[l])
        # print("22left",res, "left[l]", left[l], "l",l)
        l+=1
    while r < len(right):
        res.append(right[r])
        result.append(right[r])
        # print("22right",res, "right[r]",right[r], "r",r)
        r+=1
    # print(res)
    return res

n, k = map(int, input().split())
li=list(map(int, input().split()))

merged_li = mergeSort(li)
if len(result)<k:print(-1)
else :           print(result[k-1])
# print(merged_li)