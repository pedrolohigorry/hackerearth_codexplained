def shuffle (n, arr):
    # x_index and y_index to return values of arr
    x_index = 0
    y_index = n
    res = []
    for i in range(n):
        # first add x item, then y item, and then move both index +1
        res.append(arr[x_index])
        res.append(arr[y_index])
        x_index += 1
        y_index += 1    
    return res

n = int(input())
arr = list(map(int, input().split()))

out_ = shuffle(n, arr)
print (' '.join(map(str, out_)))
