numbers = [int(x) for x in input("plaase_enter_your_list:(plase_separate_numbers_with_spaces) ").split()]
squared_numbers = list(map(lambda x: x**2, numbers))
print("list_of_powers_of_two", squared_numbers)