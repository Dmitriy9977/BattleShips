from player import Player


class GameManager:
    def __init__(self, players):
        self.players = players
        self.atack_player = players[0]
        self.defender_player = players[1]

    def start_game(self):
        self.game()

    def end_game(self):
        print("Ура наконец-то вы закончили!")

    def game(self):
        while True:
            print("Ходит {}\n".format(self.atack_player.name), end="")
            atack_step = self.atack_player.step()
            result_step = self.defender_player.atack(atack_step)

            print(self.atack_player.name)
            Player.print_fieldandprevmoves(self.atack_player, self.defender_player)

            if result_step:
                print("{} попал!".format(self.atack_player.name))
                if self.defender_player.isLost():
                    print("Проиграл " + self.defender_player.name)
                    self.end_game()
                    return

            else:
                self.atack_player, self.defender_player = self.defender_player, self.atack_player
