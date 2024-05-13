import random


field = [['*' for _ in range(25)] for _ in range(25)]


x, y = 5, 4
field[x][y] = 'X'


item_x, item_y = random.randint(0, 24), random.randint(0, 24)

field[item_x][item_y] = 'O'


score = 0



def print_field():
    for row in field:
        print(' '.join(row))


while True:

    print_field()
    print(f'Score: {score}')


    action = input('Enter action (up/down/left/right): ')

    if action == 'up':
        if x > 0:
            field[x][y] = '*'
            x -= 1
            field[x][y] = 'X'
    elif action == 'down':
        if x < 24:
            field[x][y] = '*'
            x += 1
            field[x][y] = 'X'
    elif action == 'left':
        if y > 0:
            field[x][y] = '*'
            y -= 1
            field[x][y] = 'X'
    elif action == 'right':
        if y < 24:
            field[x][y] = '*'
            y += 1
            field[x][y] = 'X'


    if x == item_x and y == item_y:
        try:
            field[item_x][item_y] = o
        except:
            print("!")


        if field[item_x][item_y] == 'O':
            score = score + 1
            print("!!!")
        elif field[item_x][item_y] == 'S':
            score = score + 2

        field[item_x][item_y] = 'X'
        item_x, item_y = random.randint(0, 24), random.randint(0, 24)
        if random.random() < 0.1:
            field[item_x][item_y] = 'S'
            o = 'S'
        else:
            field[item_x][item_y] = 'O'
            o = 'O'

