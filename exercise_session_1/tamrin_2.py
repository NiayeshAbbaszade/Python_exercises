import random
numbre=random.randint(1,100)
while True:
        try:
            hads=int(input('adad bein 1 ta 100 vared konid'))
            if not (1<=hads<=100):
                print('ltfan beine 1 ta 100 vared konid')
                continue
            elif numbre < hads:
                print('adad vared shode az adad mored nazar bozorgtar ast')
            elif hads<numbre:
                print('adad vared shode az adad mored nazar kochaktar ast')
            else:
                print("tabrik! dorost hads zadi") 
                break
        except ValueError:
            print("lotfan adad vared konid ")             