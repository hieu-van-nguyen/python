import heapq

def topKFrequent(nums, k):
    count = {}
    for num in nums:
        count[num] = 1 + count.get(num, 0)
    heap = []
    for num in count.keys():
        heapq.heappush(heap, (count[num], num))
        if (len(heap) > k):
            heapq.heappop(heap)
    res = []
    for i in range(k):
        res.append(heapq.heappop(heap)[1])
    return res

print(topKFrequent([1,2,2,3,3,3], 2)) # [2, 3]
    