from gamemanager import GameManager
from player import Player
from strategies import BotTactics, PlayerTactics


print("Добро пожаловать в игру \"Морской Бой\"\n")
print("*************************** Правила игры **************************")
print("*********** Корабли расставляется в произвольном порядке **********")
print("********* Игрок может сам выбрать любое произвольное поле *********")
print("*Кто первый уничтожит все вражеские корабли, считается победителем*")
print("********** Попадание в корабль отмечается 'X' промах 'T' **********")
input("***************** Нажмите ENTER чтобы начать игру *****************")



# Создаем игрок и задаем им имя и их тактики
player = Player('Игрок', PlayerTactics())
bot = Player("Компьютер", BotTactics())
game = GameManager([player, bot])
game.start_game()
