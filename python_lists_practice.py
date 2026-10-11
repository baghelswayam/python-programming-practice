#Question 1:remove the Last Element

a = [10,20,30,40,50]
a.pop()
print(a)

#Question 2:remove the Specific Element

a =[10,20,30,20,40]
a.remove(20)
print(a)

#Question 3:Count an Element

a=[5,2,5,8,5,1]
x=a.count(5)
print(x)

#Add an element
a=[10,20,30]
a.append(100)
print(a)

#Insert an element
a=[10,20,30,40]
a.insert(1,99)
print(a)

#Extent a List
a=[1,2,3]
b=[4,5,6]
a.extend([b])
print(a)

#reverse a List
a=[10,20,30,40,50]
a.reverse()
print(a)

#Sort a List
a=[40,10,30,20,50]
a.sort()
print(a)

#Find the index
a=[10,30,20,30,40]
x=a.index(30)
print(x)

#Copy a List
a=[10,20,30]
b=a.copy()
b.append(100)
print(a)
print(b)

#Check the length of a list
a =[10,20,30,40,50]
print("Length of list:",len(a))

