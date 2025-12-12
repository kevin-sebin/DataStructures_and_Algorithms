# a = False
# if a == 'kevin':
#     print(True)
# else:
#     print(False)

# a = 'hello world'
# print('good', a)

# a = 'kevin'
# print(a.capitalize())

# a = 'kathy'
# b = 'i'
# print(a.find(b))

# a = 'kevin'
# print(a*a)

# a = 5
# print(a**a)

# arr = [1, 2, 3, 4, 5, 6]
# arr1 = [9, 5, 6]
# arr.extend(arr1)

# arr.insert(3, 500000)
# print(arr)


# a = [8, 3, 6, 7, 0, 2, 3, 5, 99, 0, 2]
# print(a[0:9:3])
l1=[10,20,30,40,50,60,70,80,90,100]
for i in l1:
    print(i)
l1.extend([2,3])
print(l1)
l1.sort(reverse=True)
print(l1)
s=max(l1)
print("the max value is:",s)
del(l1[1:8])
print(l1)
s=l1.count(80)
print("the count is:",s)
l1[2]=200
print(l1)
l1.clear()
print(l1)






