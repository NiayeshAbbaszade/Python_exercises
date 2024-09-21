def get_list_from_user(prompt):
    return list(map(int, input(prompt).split()))
def main():
    list1 = get_list_from_user(input("List-e aval ra vared konid (ba fasele joda konid): "))
    list2 = get_list_from_user(input("List-e dovom ra vared konid (ba fasele joda konid): "))
    if len(list1) != len(list2):
        print("List-ha bayad ham andaze bashand.")
        return
    result = list(map(lambda x, y: x + y, list1, list2))
    print("List-e natije:")
    print(result)