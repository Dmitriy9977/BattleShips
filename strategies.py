import random


def random_field():
    ships = [1, 1, 1, 1, 2, 2, 3]
    field = [[0 for i in range(6)] for i in range(6)]

    max_iter = 1000
    iter = 0
    while len(ships) != 0:
        if max_iter < iter:
            raise Exception("Не получилось создать поле")

        ship_position = [random.randrange(0, 6, 1), random.randrange(0, 6, 1)]
        if field[ship_position[0]][ship_position[1]] != 0:
            iter += 1
            continue

        ship_length = ships[-1]
        ship_directions = random.randrange(0, 4, 1)  # 0 - вниз, 1 - вверх, 2 - вправо, 3 - влево
        if ship_directions == 0 and ship_position[0] + ship_length < 6 and 0 == sum(
                [row[ship_position[1]] for row in field[ship_position[0]: ship_position[0] + ship_length]]):
            if ship_position[0] - 1 >= 0:
                for i in range(-1, 2):
                    if ship_position[1] + i < 6 and ship_position[1] + i >= 0:
                        field[ship_position[0] - 1][ship_position[1] + i] = 3
            for i in range(0, ship_length):
                field[ship_position[0] + i][ship_position[1]] = 1
                if ship_position[1] - 1 >= 0:
                    field[ship_position[0] + i][ship_position[1] - 1] = 2
                if ship_position[1] + 1 < 6:
                    field[ship_position[0] + i][ship_position[1] + 1] = 2
            if ship_position[0] + ship_length < 6:
                for i in range(-1, 2):
                    if ship_position[1] + i < 6 and ship_position[1] + i >= 0:
                        field[ship_position[0] + ship_length][ship_position[1] + i] = 4

        elif ship_directions == 1 and ship_position[0] - ship_length >= 0 and 0 == sum(
                [row[ship_position[1]] for row in field[ship_position[0] - ship_length: ship_position[0] + 1]]):
            if ship_position[0] + 1 < 6:
                for i in range(-1, 2):
                    if ship_position[1] + i < 6 and ship_position[1] + i >= 0:
                        field[ship_position[0] + 1][ship_position[1] + i] = 4
            for i in range(0, ship_length):
                field[ship_position[0] - i][ship_position[1]] = 1
                if ship_position[1] - 1 >= 0:
                    field[ship_position[0] - i][ship_position[1] - 1] = 2
                if ship_position[1] + 1 < 6:
                    field[ship_position[0] - i][ship_position[1] + 1] = 2
            if ship_position[0] - ship_length >= 0:
                for i in range(-1, 2):
                    if ship_position[1] + i < 6 and ship_position[1] + i >= 0:
                        field[ship_position[0] - ship_length][ship_position[1] + i] = 3

        elif ship_directions == 2 and ship_position[1] + ship_length < 6 and 0 == sum(
                field[ship_position[0]][ship_position[1]:ship_position[1] + ship_length]):
            if ship_position[1] - 1 >= 0:
                for i in range(-1, 2):
                    if ship_position[0] + i < 6 and ship_position[0] + i >= 0:
                        field[ship_position[0] + i][ship_position[1] - 1] = 3
            for i in range(0, ship_length):
                field[ship_position[0]][ship_position[1] + i] = 1
                if ship_position[0] + 1 < 6:
                    field[ship_position[0] + 1][ship_position[1] + i] = 2
                if ship_position[0] - 1 >= 0:
                    field[ship_position[0] - 1][ship_position[1] + i] = 2
            if ship_position[1] + ship_length < 6:
                for i in range(-1, 2):
                    if ship_position[0] + i < 6 and ship_position[0] + i >= 0:
                        field[ship_position[0] + i][ship_position[1] + ship_length] = 4

        elif ship_directions == 3 and ship_position[1] - ship_length >= 0 and 0 == sum(
                field[ship_position[0]][ship_position[1] - ship_length:ship_position[1]]):
            if ship_position[1] + 1 < 6:
                for i in range(-1, 2):
                    if ship_position[0] + i < 6 and ship_position[0] + i >= 0:
                        field[ship_position[0] + i][ship_position[1] + 1] = 4
            for i in range(0, ship_length):
                field[ship_position[0]][ship_position[1] - i] = 1
                if ship_position[0] + 1 < 6:
                    field[ship_position[0] + 1][ship_position[1] - i] = 2
                if ship_position[0] - 1 >= 0:
                    field[ship_position[0] - 1][ship_position[1] - i] = 2
            if ship_position[1] - ship_length >= 0:
                for i in range(-1, 2):
                    if ship_position[0] + i < 6 and ship_position[0] + i >= 0:
                        field[ship_position[0] + i][ship_position[1] - ship_length] = 3
        else:
            iter += 1
            continue

        iter += 1
        ships.pop()

    field = [[i if i < 2 else 0 for i in row] for row in field]

    if sum([sum(row) for row in field]) != 11:
        raise Exception("Неправильное поле!")

    return field


class PlayerTactics:
    def __init__(self):
        while True:
            try:
                self.field = random_field()

                indexes = ['0', '1', '2', '3', '4', '5']
                j = 0
                print("  ", end="")
                print('  '.join(indexes))
                for row in self.field:
                    print(j, end=" ")
                    print('  '.join([str(i) for i in row]))
                    j += 1
                print("Вам нравится это поле?(y/n)", end="")
                if input() == 'y':
                    break

            except:
                continue

    def action(self):
        while True:
            try:
                x, y = input('Введите координаты через пробел: ').lower().split(' ')
                return (int(x), int(y))
            except:
                continue

    def again_action(self):
        print("Вы уже делали ход в эту точку, введите другие значения: ", end="")
        return self.action()


class BotTactics:
    def __init__(self):
        while True:
            try:
                self.field = random_field()
                break
            except:
                continue

    def action(self):
        step = random.randrange(0, 6, 1), random.randrange(0, 6, 1)
        print(step)
        return step

    def again_action(self):
        self.action()