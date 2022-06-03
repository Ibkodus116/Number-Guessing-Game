import random
num = random.randrange(0, 10)
count = 0


def game(the_num):
    global count
    count += 1
    if count == 1:
        print('if you get it right on this first try your point will be %d \n' % point)
    else:
        print('if you get it right this time, your total point will be %d \n' % point)

    game_status = False
    while game_status == False:

        try:
            print('___________________________________________')
            player_num = int(input('guess a number between 0 - 10\n'))
            if player_num <= 10:
                game_status = True

            else:
                print('the number is above the required number \n')

        except ValueError:
            print('you have entered a wrong input \n')

    if player_num == the_num:
        print('congratulations you guessed the correct number\n')
        print("Total point scored is %d" % point)
        exit()

    else:
        if count == 3:
            print('You have guessed the wrong Number \n')
            print('And exceeded your number of try\n')
        else:
            print('\n you have guessed wrongly please try again')
            start(the_num)


def hint(the_num):

    if (the_num % 2) == 0:
        print('Hint1: it is a Even Number \n')

    else:
        print('Hint1: it is an Odd Number \n')
    game(the_num)


def hint_two(the_num):

    if the_num >= 0 and the_num <= 5:
        print('Hint2: The Number is between 0-5 \n')
    elif the_num >= 6 and the_num <= 10:
        print('Hint2: The Number is between 6-9 \n')
    else:
        print("olodo")
    game(the_num)


def hint_three(the_num):
    n = random.randrange(1, 85)
    print('This is your Final Hint\n')
    ans = the_num * n
    print('Hint2: The Number multiplied by %d is %d\n' % (n, ans))
    game(the_num)


def start(the_num):
    global point
    if count == 0:
        point = 50
        hint(the_num)
    if count == 1:
        point = 40
        hint_two(the_num)
    if count == 2:
        point = 20
        hint_three(the_num)
    else:
        point = 0
        print("You are out of the Game the correct number is %d\n" % the_num)
        print("your total point is %d\n" % point)
        exit()


start(num)