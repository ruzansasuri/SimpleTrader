import re
from collections import namedtuple
from trader_sorting import sortlist

def file_check(file,perm):
    try:
        f = open(file,perm)
        return f
    except FileNotFoundError:
        print("File",file,"does not exist...")
        exit()
def create_dict(file):
    amts = namedtuple('amts', ['n','cost'])
    items = dict()
    for line in file:
        if not re.search(r".*\s[0-9]*\s[0-9]*", line):
            print("Enter the details in the correct format in the file...(item number cost)")
            exit()
        list = line.split()
        if int(list[1]) < 0:
            print("Item quantity should not be less than zero.")
            exit()
        if list[0] in items.keys() :
            print("You have entered a particular item twice in one of the files.")
            exit()
        if int(list[2]) < 0:
            print("Item price should not be less than zero.")
            exit()
        items[list[0]] = amts(int(list[1]),int(list[2]))
    return items

def validate(dict1,dict2):
    for item in dict1:
        if item not in dict2.keys():
            print(item, " does not exist in the other village so can't calculate.")
            exit()
    for item in dict2:
        if item not in dict1.keys():
            print(item, "does not exist in the other village so can't calculate.")
            exit()

def profit(dict1,dict2):
    items = []
    for item in dict1:
        profit = dict2[item].cost - dict1[item].cost
        items.append((item,profit,dict1[item].n))
    items = sortlist(items)
    return items

def total_profit(items,n):
    p = 0
    for item in items:
        if item[1] <= 0:
            break
        if item[2] > n:
            p += item[1] * n
            break
        else:
            p += item[1] * item[2]
            n -= item[2]
        if n == 0:
            break
    return p

def printit(town_name,town_items,n):
    print("Go to",town_name,"and buy:")
    for item in town_items:
        if item[1] <= 0:
            break
        if item[2] > n:
            print(n,item[0],'for a profit of',item[1]*n)
            break
        else:
            print(item[2], item[0], 'for a profit of', item[1]*item[2])
            n -= item[2]
        if n == 0:
            break


def main():
    max = int(input("Maximum number of items you can carry: "))
    if max <= 0:
        print("The maximum capacity should be greater than zero")
        exit()
    first = input("Enter the file name for the first town: ")
    ffile = file_check(first,'r')
    second = input("Enter the file name for the second town: ")
    sfile = file_check(second, 'r')
    #max = 10
    #ffile = open("hilltown.txt")
    #sfile = open("valleydale.txt")
    ftown = ffile.readline().strip()
    stown = sfile.readline().strip()
    fdict = create_dict(ffile)
    sdict = create_dict(sfile)
    validate(fdict,sdict)
    profits1 = profit(fdict,sdict)
    profits2 = profit(sdict, fdict)
    tp1 = total_profit(profits1, max)
    tp2 = total_profit(profits2, max)
    if tp1 >= tp2:
        printit(ftown,profits1,max)
        print('\nIncome from this trade is',tp1)
    if tp1 == tp2:
        print("\nOR\n")
    if tp1 <= tp2:
        printit(stown, profits2,max)
        print('\nIncome from this trade is', tp2)

if __name__ == '__main__':
    main()