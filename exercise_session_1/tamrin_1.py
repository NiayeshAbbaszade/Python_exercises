while True :
    try:
        age=int(input("enter_your_age"))
        if age >= 18 :
            print('you_can_vote')
        else:
         print("you_can_not_vote")
         break
    except ValueError:
        print('plese_enter_correct_number')       