def sort_square (n, arr):
    # left and right are indexes to start from the left and right of arr.
    left = 0
    right = n-1
    res = []
    for i in range(n):
        # Check which item of arr is bigger: leftmost or rightmost.
        # Biggest is added to res and index (left or right) increased.
        if abs(arr[left])>abs(arr[right]): 
            res.insert(0, arr[left]**2)
            left += 1
        else:
            res.insert(0, arr[right]**2)
            right -= 1
    return res

n = int(input())
arr = list(map(int, input().split()))

out_ = sort_square(n, arr)
print (' '.join(map(str, out_)))
