def minimum(arr, size):
    temp = arr[0]
    for i in range(1, size):
        temp = min(temp, arr[i])
    return temp

def maximum(arr,size):
    temp = arr[0]
    for i in range(1, size):
        temp = max(temp, arr[i])
    return temp

a = [1,5,9,8,2]
print('Minimum value:', minimum(a,len(a)))
print('Maximum value:', maximum(a,len(a)))