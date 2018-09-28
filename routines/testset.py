
def uniqueList(list1, list2):
    uniqueList = []


    for element in list2:
        if(element not in list1):
            uniqueList.append(element)
    for element in list1:
        if(element not in list2):
            uniqueList.append(element)
    
    return uniqueList,set(list1 + list2)

print(uniqueList([1,2,3,4],[2,3,4,5,6]))