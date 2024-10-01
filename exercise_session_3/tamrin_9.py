list1 = list(map(int, input("List aval ra vared konid (ba fasele joda konid): ").split()))
list2 = list(map(int, input("List dovom ra vared konid (ba fasele joda konid): ").split()))
result = list(map(lambda x, y: x + y, list1, list2))
print("List natije: ", result)