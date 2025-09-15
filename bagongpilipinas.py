# LIST [] = ordered/mutable can have duplicate
# TUPLE () = ordered/immutable can have duplicate
# DICTIONARY {} = unordered key:value pair cannot have duplicated
# id=1118 name="mike"

#LIST
# mylist =[]
# mylist = ["mike","acosta","esteron"]
# mylist = ["mike", 90.50, "emerson", 80.20, "naniong", 80.20]
# print(mylist[1])
# print(mylist[:5])
# print(mylist[::-1])

#change
# mylist[0]="justin"
# mylist[:2]="james"

# print(mylist)
# print(mylist[0])

# ADD VALUE to the end of the list
# mylist.append("berbon")
# print(mylist)
#add value to the front of the list
# mylist.insert(0,"pico")
# print(mylist)
# mylist.pop()
# mylist.pop(0)
# print(mylist)
# mylist.remove("berbon")
# print(mylist)
# for x in mylist:
#     print(f"{x}", end=" ")
# print()
# for x in range(len(mylist)):
#     print(f"{mylist[x]}", end=" ")
# print()


# should be the same data type in order to work
# mylist.sort
# print(mylist)
# mylist.reverse
# print(mylist)

# myList=[[1,4,10,2],[5,1,11,6]]
# print(myList[0][2])

# for x in range(len(myList)):
#     print(f"row {x}")
#     myList[x].sort()
#     for y in range(len(myList[x])):
#         print(myList[x][y], end=" ")
#     print()

# one dimentional

# mylist=[]
# for x in range(5):
#     print("Enter Score: ")
#     num = float(input())
#     mylist.append(num)
# print(mylist)

# 2 dimentional

# ASSIGNMEN: searching
# nestedlist=[]
# row = int(input("Row: "))
# col = int(input("col: "))

# for x in range(row):
#     print(f"Row {x+1}")
#     innerList=[]
#     for y in range(col):
#         print(f"Enter Score{y+1}: ")
#         score = str (input())
#         innerList.append(score)
#     nestedlist.append(innerList)
# print(nestedlist)
# search = int(input("enter num: "))
# for x in range(row):
#     if search in nestedlist[x]:
#         y = nestedloop[x].index(search)
#         print(f"Found "{search})

# TUPLE
# mytuple =()
# mytuple=("mike", "esteron", "Acosta")
# tuplelist=list(mytuple)
# tuplelist[0]="micheal"
# tuplelist.append("naniong")
# tuplelist.pop()
# mytupletwo = tuple(tuplelist)
# print(mytupletwo)


# dictionary
# dictionary={}
# mydict={"id":"URA-0999", "name":"mike acosta", "salary":1500.00}
# print(mydict["name"])
# mydict["name"]="james luzan"
# print(mydict["name"])
# mydict["age"]=69
# print(mydict.keys())
# print(mydict.values())

# for x,y in mydict.items():
#     print(f"key: {x}, value:{y}", end=" ")
