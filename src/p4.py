def intersection(list1, list2):
    result = [] 

    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                if list1[i] not in result:
                    result.append(list1[i])
    return result