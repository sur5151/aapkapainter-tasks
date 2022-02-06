# Write a code that prints out the first occurrence of a duplicate in a given array of integers
# Sample Input: [1,2,3,2,1,1]
# Output: 2
l = list
def f1(l):
    max  = len (l)
    idx = 0
    final = False
    l1 = []
    for i in range(0, max):
        for j in range(i+1, max):
            if l[i] == l[j] and j < max:
                idx = j
                l1.append(idx)
        a= sorted(l1)

        final = a[0]
    if idx != 0:
        print("The first occured duplicate no is {}".format(l[final]))
    else:

        print ("No duplicate found")


a = [1, 2,5, 5 , 2, 1]
# a = [10,20,30,20,10,10]
f1(a)