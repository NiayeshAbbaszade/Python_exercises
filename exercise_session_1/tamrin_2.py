import random
Number = random.randint(1,100)

while True :
    try:
        guss=int(input('enter_your_number'))
        if Number >= guss :
            print('the_number_is_larger')
        elif Number<=guss:
            print('the_number_is_smaller')
        else:
            print('very_nice_your_gussed_right')
        break
    except ValueError :
        print('plaese_enter_correct_number')
