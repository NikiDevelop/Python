def binary_search(list,item):
    first = 0
    last = len(list) - 1
    found = False
    while (first <= last and not found):
        mid = (first + last) // 2
        if list[mid] == item:
            found = True
        else:
            if item < list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found


num_list = [4,7,12,45,52,71,28,10]
print("List has the items:",num_list)

searchNum = int(input("Enter a number to search for: "))
found = binary_search(num_list,searchNum)

if found == True:
    print(searchNum,"is present in the list")
else:
    print(searchNum,"is not found in the list")
