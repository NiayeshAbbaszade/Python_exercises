import random

number_to_guess = random.randint(1, 100)
while True:
    try:
        user_guess = int(input("yek adad bein 1 ta 100 hads bezanid: "))
        if user_guess < 1 or user_guess > 100:
            print("lotfan adadi bein 1 ta 100 vared konid.")
        elif user_guess > number_to_guess:
            print("adad mored nazar bozorgtar ast.")
        elif user_guess < number_to_guess:
            print("adad mored nazar koochaktar ast.")
        else:
            print(f"tabrik! adad dorost ra hads zadid: {number_to_guess}")
            break
    except ValueError:
        print("lotfan yek adad motabar vared konid.")