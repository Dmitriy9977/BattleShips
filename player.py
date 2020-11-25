class Player:  # создаем класс игрока
    def __init__(self, name, tactics):
        self.name = name
        self.tactics = tactics  # ход игрока
        self.field = tactics.field  # создание поля и расставление кораблей и добавляются в список ships
        self.prev_moves = [[0 for i in range(6)] for i in range(6)]  # матрица предыдущих ходов

    def step(self):
        position = self.tactics.action()
        while self.prev_moves[position[0]][position[1]] != 0:
            position = self.tactics.again_action()

        self.prev_moves[position[0]][position[1]] = 1  # запоминаем клетку в которую уже походили
        return position  # Куда походим

    def atack(self, position):
        if self.field[position[0]][position[1]] == 1:
            self.field[position[0]][position[1]] *= -1  # инвертируем число если подбили корабль
            return True
        return False

    def isLost(self):
        return 11 == -sum([sum(row) for row in self.field])

    def print_field(self):
        indexes = ['0', '1', '2', '3', '4', '5']
        j = 0
        print("  ", end="")
        print('  '.join(indexes))
        for row in self.field:
            print(j, end=" ")
            print('  '.join([str(i) for i in row]))
            j += 1

    def print_prevmoves(self):
        indexes = ['0', '1', '2', '3', '4', '5']
        j = 0
        print("  ", end="")
        print('  '.join(indexes))
        for row in self.prev_moves:
            print(j, end=" ")
            print('  '.join([str(i) for i in row]))
            j += 1

    def print_all_field(self):
        indexes = ['0', '1', '2', '3', '4', '5']
        j = 0
        print('*****Ваше поле*****', end="\t\t *Поле противника*\n")
        print("  ", end="")
        print('  '.join(indexes), end="\t")
        print("  ", end="")
        print('  '.join(indexes))

        for row in range(6):
            print(j, end=" ")
            print('  '.join([str(i) for i in self.field[row]]), end="\t")
            print(j, end=" ")
            print('  '.join([str(i) for i in self.prev_moves[row]]))
            j += 1

    @staticmethod
    def print_fieldandprevmoves(atackplayer, defenderplayer):

        field_values = {0: '0', 1: '1', -1: 'X'}
        moves_values = {-1: 'X', 0: '0', 1: 'T'}

        atack_field = defenderplayer.field
        miss_field = atackplayer.prev_moves

        j = 0

        indexes = ['0', '1', '2', '3', '4', '5']
        print('  ' + ' '.join(indexes), end="\t")
        print('  ' + ' '.join(indexes))

        for row in range(6):
            print(j, end=" ")
            for i in range(6):
                item = atackplayer.field[row][i]
                print(field_values[item], end=" ")
            # print('  '.join([ str(i) for i in atackplayer.field[row]]), end="\t")

            print("\t" + str(j), end=" ")

            for i in range(6):
                item = miss_field[row][i] if atack_field[row][i] != -1 else atack_field[row][i]
                print(moves_values[item], end=" ")
            print()
            j += 1