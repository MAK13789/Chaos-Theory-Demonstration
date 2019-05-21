def list1(x):
    list1 = []
    list1.append(1)
    list1.append(1)
    for i in range(2, x):
        temp = list1[i-2] + list1[i-1]
        list1.append(temp)
    return(list1)
list1 = (list1(100))
list2 = []
list2.append(1)
list2.append(1)
list2.append(1)
for j in range(3, len(list1)):
    temp = list1[j-1]
    list2.append(temp)
print (list1)
print (list2)
list3 = []
for k in range(len(list2)):
    list3.append(k+1)
print (list3)
list4 = []
for a in range(0, len(list2)):
    temp = list1[a] - list2[a]
    list4.append(temp)
print (list4)
    
