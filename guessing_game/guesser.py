import random
print("#####Guesses#####".center(100))

real_number = random.randint(0,100)
tries = 10
c = 0
while True:
    c+=1
    find = int(input(f'find the number:'))
    if find == real_number:
        print(f"found at {c} tries the number is {real_number}")
        break
    elif real_number > find:
        print('The number is larger')
    elif real_number < find:
        print('The number is lower')
    elif c == tries:
        print(f"TRY AGAIN NEXT TIME the number was {real_number}")
        break