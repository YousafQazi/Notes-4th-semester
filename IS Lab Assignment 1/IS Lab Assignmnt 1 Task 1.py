list1 = input("ENTER THE ELEMENTS OF FIRST LIST : ").split()
list2 = input("ENTER THE ELEMENTS OF SECOND LIST : ").split()
list1 = [int(a) for a in list1]
list2 = [int(a) for a in list2]
merged = list1 + list2
merged.sort()
print("Merged and Sorted List: ", merged)

