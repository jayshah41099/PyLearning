# create a list in python
PythonList = ["banana", "apple", "Orange"] # string  value list
PyList = [10, 23, 45, 34, 45, 56, 23, 11, 29, 49] # numeric list
AList = ["banana", "apple", "Orange", "banana", "apple", "Pineapple"] # repeatative content list
BoolList = [True, False, False, True, False] # Bool list
MixedList = ["hello", 23, True, "proper", False, 38] # mixed data type list
print(PythonList)
print(PyList)
print(AList)
print(BoolList)
print(MixedList)

# create a list of 10 Nones using minimalist writing
l = [None] * 10
print (len(l))
print(l)

# length of the list
print(len(MixedList)) # indexing starts from 0 but length count starts from 1

# finde the data type of the list
print(type(BoolList))

# using list constructor list() to create a list
Blist = list(("hello", True, 24))
print(Blist)

# Acces list using indexing
print(Blist[1]) # positive indexing
print(Blist[-2]) # negative indexing

# print list using range of indexing
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[-4:-1]) # negative indexing doesn't mea you can print the list in reverse order like -1:-4

# print the list up to the index (index stop value not include)
print(thislist[:4])

# print the list starting from this point till end
print(thislist[2:])

# using in keywork for checking item exists in the list
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# change single value from the list without creating new list
print(thislist)
thislist[3] = "Pineapple"
print(thislist)

# replace index 1, 2 and 3 with following numbers and print it out the list. - (Don't create new list)
aList = [4, 8, 12, 16]
print(aList)
aList[1:4] = [20,24,28]
print(aList)

# replacing multiple index with single value (it will reduce the list length as well)
print(thislist, len(thislist))
thislist[1:3] = ["watermelon"]
print(thislist, len(thislist))

# using insert() method to change the value at specified index
Clist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(Clist, len(Clist))
Clist.insert(2, "Watermelon")
print(Clist, len(Clist))

# using append() to add value at the end of the list
Clist.append("orange")
print(Clist, len(Clist))

# add a list to another list using extend() method
Dlist = [10, 23, 45, 34]
Elist = [34, 34, 67, 46, 57]
tuplelist = (20, 34) # tuplet
print(Dlist, len(Dlist), Elist, len(Elist))
Dlist.extend(Elist)
print(Dlist, len(Dlist), Elist, len(Elist))
Elist.extend(tuplelist) # Adding tuplet in the list
print(Elist, len(Elist))

# remove specific value from the list using remove()
print(thislist, len(thislist))
thislist.remove("Pineapple")
print(thislist, len(thislist))

# using pop() method to remove specific index value from the list - if no index mentioned removes last item
print(thislist, len(thislist))
thislist.pop(1)
print(thislist, len(thislist))
thislist.pop() # no index last item in the list removed
print(thislist, len(thislist))

#empty out the list with one line of code
cList = [10, 20, 30, 40]
del cList[0]
print(cList, len(cList))
del cList[0:3]
print(cList, len(cList))

# using clear() method to empty out the list
fList = [10, 20, 30, 40]
print(fList)
fList.clear()
print(fList)

# printing each value of the list using for and while loop
gList = [10, 20, 30, 40]
[print(x) for x in gList]

'''
for x in gList:
    print(x)

for i in range(len(gList)):
  print(gList[i])

i = 0
while i < len(gList):
  print(gList[i])
  i = i + 1
'''

# multiply the each charcter of list by 2 use minimal writing 
IList = [1, 2, 3, 4, 5, 6, 7]
pow2 = [2* x for x in IList]
print(pow2)

'''


# Question 5 - print out following list as a single string.
myList = ["Hello", "Python"]
print(" ".join(myList))


'''