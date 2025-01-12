import heapq

# Approach 1, do a sort and get the Kth largest element.
def kth_largest_using_sort(arr, k):
    arr.sort()
    return arr[k-1]

arr = [7,1,2,5,1,4]
print(kth_largest_using_sort(arr, 4))


# Approach 2, use a min heap priority queue to find the Kth largest element
def kth_largest_using_heap(arr, k):
    priority_queue = []

    for i in range(len(arr)):
        heapq.heappush(priority_queue,arr[i])

        if len(priority_queue) > k:
            heapq.heappop(priority_queue)

    return priority_queue[0]

arr = [0,1,14,542,12,53,7]
print(kth_largest_using_heap(arr,5))