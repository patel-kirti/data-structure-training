import heapq

heap=[]
nums=[3,9,7,5,11,20,15,8,17]

heapq.heapify(nums)
print("Create heap :",end=" ")
print(list(nums))
print("Push element :",end=" ")
heapq.heappush(nums,4)
print(list(nums))
print("Poped smallest element :",end=" ")
print(heapq.heappop(nums))
print(list(nums))

# for num in nums:
#     heappush(heap,num)
#
# while heap:
#     print(heappop(heap))
#
# heapify(nums)
# print(nums)