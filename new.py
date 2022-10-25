import random

guess_num = random.randint(1, 10)

while True :
    print('''
1. factors of a number
2. guess game (not working)
3. sum of 1 to your num
4.quit
''')

    hi = input(": ")


    def factors(num):
        x = []
        y = []

        for i in range(1, int(num)):
            x.append(i)
        for s in x:
            if int(num) % s == 0:
                y.append(s)
        print(f"the factors of {num} are {y}")


    if int(hi) == 1:
        factors(input("what number factors did you want : "))

    if int(hi) == 2:
        print('''
        rules :
        1. you have 3 chance
        2. guess number between 1 to 10
        
        ''')
        guess_count = 0
        guess_limit = 3

        while guess_count < guess_limit:
            input_num = input("What is your guess number : ")
            guess_count += 1
            if input_num == guess_num:
                print('Yes, you did it !')
                break
            else:
                print("Try again!")

        if guess_count >= guess_limit:
            print(f'oh! no your lost , the guess number is {guess_num}')
            print('Please, try again! better luck next time')

    if int(hi) == 3:
    	q = input('Enter your number : ')
    	w = int(q)+1
    	e= range(1,w)
    	r= sum(e)
    	print(r)
    if int(hi) == 4 :
        break

    elif int(hi) <=5  :
        print('please enter only given number only')
