# Sort the list using sort() method - It is casesensative and places uppercase before lowercase
List1 = ["Orange", "Mango", "Kiwi", "banana"]
List2 = [23, 34, 12, 22, 1, 45, 7, 61]
List1.sort()
print(List1, "\ncasesensative sort() method places Uppercase before lowercase")
print(sorted(List2), "\n Sorted doesn't store the sorted lis tin the same variable compare to sort()\n", List2)

# sorting a list in descending order
List1.sort(reverse=True)
print(List1)
print(sorted(List2, reverse=True))

# sort the list based on how close the number is to 50.
def myfunc(n):
  return abs(n - 50)

List3 = [100, 50, 65, 82, 23]
List3.sort(key = myfunc)
print(List3)

# perform case - insensitive sort of the list
List1.sort(key = str.lower)
print(List1)

# use reverse method to sort list in descending order
List1.reverse()
print(List1)
