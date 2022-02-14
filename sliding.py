# def sliding(arr,k):
#    start=0
#    curr=0
#    maxi=0
#    for i in range(len(arr)):
#        curr+=arr[i]
#        if curr >= k:
#            if curr == k:
#                if maxi < i-start+1:
#                    maxi=i-start+1
#                    res=[start,i]
#            while curr>=k:
#                 curr-=arr[start]
#                 start+=1
#    return res

# print(sliding([4,1,1,1,2,3,5],5))

# def pickToys(s):
#     start=0
#     d={}
#     maxi=0
#     for i in range(len(s)):
#         if s[i] not in d:
#             d[s[i]]=0
#         d[s[i]]+=1
#         while(len(d)>2):
#             d[s[start]]-=1
#             if d[s[start]]==0:
#                 d.pop(s[start])
#             start+=1
#         maxi=max(maxi,i-start+1)
#     return maxi
# print(pickToys("bac"))

# def mergeSort(n):
#     if len(n)==1:
#         return n
#     left=mergeSort(n[0:len(n)//2])
#     right=mergeSort(n[len(n)//2:])
#     merged=[]
#     i,j=0,0
#     while i<len(left) and j<(len(right)):
#         if left[i]<right[j]:
#             merged.append(right[j])
#             j+=1
#         else:
#             merged.append(left[i])
#             i+=1
#     while i<len(left):
#         merged.append(left[i])
#         i+=1
#     while j<len(right):
#         merged.append(right[j])
#         j+=1
#     return merged
# print(mergeSort([2,4,5,6,2,1,4,1,1,5]))

         
