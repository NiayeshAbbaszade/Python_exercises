n = int(input("Tedade tuple ha ra vared konid: "))
tuples_list = []
for _ in range(n):
    tup = tuple(map(int, input("Tuple ra vared konid (ba fasele joda konid): ").split()))
    tuples_list.append(tup)
sorted_list = sorted(tuples_list, key=lambda x: x[1])
print("List-e moratab shode:", sorted_list)
