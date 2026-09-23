def rev(arr):
    reversed_array = []

    while len(arr) > 0:
        reversed_array.append(arr[-1])
        arr.pop()

    return reversed_array

x = [1,2,3,4,5,6,7,8,9]


print('Original Array =',x)

print('Reversed Array =', rev(x))