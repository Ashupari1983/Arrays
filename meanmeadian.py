def mean(arr, arr_size):

    sum = 0
    for i in range (0, arr_size):
        sum += arr[i]

    return float(sum/arr_size)

def median(arr, arr_size):

    sorted(arr)

    if arr_size % 2 != 0:
        return float(arr[int(arr_size/2)])
    else:
        return float((arr[int((arr_size-1)/2)] + arr[int(arr_size/2)])/2)

a = [1,5,7,9,2,5]
size = len(a)

print(mean(a,size))
print(median(a,size))