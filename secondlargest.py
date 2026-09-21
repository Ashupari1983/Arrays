def second_largest(a,size):

    largest = secondlargest = -2147483648

    for i in range(size):

        if a[i]>largest:
            secondlargest = largest
            largest = a[i]

        elif a[i]>secondlargest and a[i]!= largest:
            secondlargest = a[i]

    print(secondlargest)

h = [1,8,4,5,3]
s = len(h)
second_largest(h,s)

