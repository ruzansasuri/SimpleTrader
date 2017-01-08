def sortlist(lists):
    if len(lists) == 1:
        return lists
    lists1 = sortlist(lists[:len(lists) // 2])
    lists2 = sortlist(lists[len(lists) // 2:])
    lists = []
    iterator1 = 0
    iterator2 = 0
    while iterator1 < len(lists1) and iterator2 < len(lists2):
        if lists1[iterator1][1] > lists2[iterator2][1]:
            lists.append(lists1[iterator1])
            iterator1 += 1
        else:
            lists.append(lists2[iterator2])
            iterator2 += 1
    if iterator1 < len(lists1):
        lists += lists1[iterator1:]
    elif iterator2 < len(lists2):
        lists += lists2[iterator2:]
    return lists
if __name__ == '__main__':
    lists = [('Cookpots', -11, 2), ('Swords', 1, 10), ('Donkeys', 0, 1)]
    print(sortlist(lists))
