import time, random

class Game:
        def __init__(self):
                self.turn = 1000

class Player:
        def poptoons_list(self):
                self.toons_list = []
                for name,toon in self.toons.items():
                        self.toons_list.append(toon.name)
        def __init__(self, name):
                self.name = name
                self.toons = {
                        "Bob":Bob()
                }
                self.toons_list = [] 
                self.inventory = [] # unused
                self.currency = 0 # unused
                self.squad = [] 
                self.poptoons_list() 

class EnemyPlayer:
        def spawnMonsters(self, integer):
                while len(self.squad) < integer:
                        monster_name = random.choice(list(self.toons.values())).name
                        if not monster_name in self.squad:
                                self.squad.append(monster_name)
        def clearSquad(self):
                self.squad = []
        def __init__(self):
                self.toons = {
                        "George":Monster1("George"), #dictionary of toons
                        "Edgar":Monster1("Edgar"),
                        "Frank":Monster1("Frank")
                }
                #squad is a list of names of monsters. they must be the same as the keys in the
                #dictionary self.toons. the monster names must be unique 
                self.squad = []

class Bob:
        def __init__(self):
                self.name = "Bob"
                self.level = 1
                self.EXP = 0
                self.actions = ["Punch", "Kick", "Run"]
                #self.status = [] #status effects
                self.items = []
                self.HP = 100
                self.HP_max = self.HP
                self.energy_max = 10 #unused
                self.energy = 10 #unused
                self.attack_def = 12
                self.attack = 12 
                self.defense_def = 5
                self.defense = 5 
                self.speed_def = 100
                self.speed = 100
                self.ATB = 0
        def target(self):
                target = input("Choose a target:")
                if target in enemy.squad:
                        return enemy.toons[target]
                else:
                        print("Target not found!")
        def fight(self):
                print(self.name + "'s turn!")
                print("Options: ", end="")
                print(self.actions)
                print("\n")
                choice = input()
                if not choice in self.actions:
                        print("Sorry, select another option.")
                        self.fight()
                elif choice == "Punch":
                        self.punch(self.target())
                elif choice == "Kick":
                        self.kick(self.target())
                elif choice == "Run":
                        endBattle()
        def punch(self, target): 
                try:
                        target.HP -= (self.attack + random.randrange(-2, 2))
                        if target.HP <= 0:
                                for i in range(len(enemy.squad)):
                                        if enemy.squad[i] == enemy.toons[target.name].name:
                                                del enemy.squad[i]
                                                break
                except AttributeError:
                        self.punch(self.target())
        def kick(self, target):
                try:
                        target.HP -= (self.attack + random.randrange(-3, 3))
                        if target.HP <= 0:
                                for i in range(len(enemy.squad)):
                                        if enemy.squad[i] == enemy.toons[target.name].name:
                                                del enemy.squad[i]
                                                break
                except AttributeError:
                        self.kick(self.target())

class Monster1:
        def __init__(self, name):
                self.name = name
                self.level = 1
                self.EXP_drop = 50
                self.actions = ["Punch", "Kick"]
                self.status = []
                self.HP = 100
                self.HP_max = self.HP
                self.energy = 10 #unused
                self.attack = 4
                self.defense = 3
                self.speed = 100
                self.ATB = 0
        def fight(self):
                choice = random.choice(self.actions)
                target = random.choice(player.squad)
                if choice == "Punch":
                        print(self.name + " punch!")
                        player.toons[target].HP -= self.punch()
                        if player.toons[target].HP <= 0:
                                for i in range(len(player.squad)):
                                        if player.squad[i] == player.toons[target].name:
                                                del player.squad[i]
                                                break
                elif choice == "Kick":
                        print(self.name + " kick!")
                        player.toons[target].HP -= self.kick()
                        if player.toons[target].HP <= 0:
                                for i in range(len(player.squad)):
                                        if player.squad[i] == player.toons[target].name:
                                                del player.squad[i]
                                                break
        def punch(self):
                return (self.attack + random.randrange(-1, 0))
        def kick(self):
                return (self.attack + random.randrange(-2, 1))

def mainMenu(): #main menu
        newWindow()
        print("Hero: "+player.name)
        print("Toons:", end=" ") 
        print(player.toons_list)
        print("Current Squad: "+str(player.squad))
        print("Options: Fight Squad Quit\n")
        menu = input().lower()
        if menu == "fight":
                startBattle(2)
        elif menu == "squad":
                squadManage()
        elif menu == "quit":
                quitGame()
        else:
                print("Please select another option.")
                mainMenu()

def startBattle(monsters): # TODO make this flow cleaner
        newWindow()
        enemy.spawnMonsters(monsters) #spawns 2 monsters for testing
        while player.squad and enemy.squad:
                battleRound()
        endBattle()

def endBattle():
        newWindow()
        print("Battle over!")
        enemy.clearSquad()
        for i in player.toons.values():
                i.HP = i.HP_max
                i.ATB = 0
        for i in enemy.toons.values():
                i.HP = i.HP_max
                i.ATB = 0
        mainMenu()

def battleRound():
        newWindow()
        if not player.squad or not enemy.squad: 
                endBattle()
        else:
                for i in player.squad:
                        player.toons[i].ATB += player.toons[i].speed
                        if player.toons[i].ATB >= game.turn:
                                battleInfo()
                                player.toons[i].fight()
                for i in enemy.squad:
                        enemy.toons[i].ATB += enemy.toons[i].speed
                        if enemy.toons[i].ATB >= game.turn:
                                battleInfo()
                                enemy.toons[i].fight()

def battleInfo():
        for i in player.squad:
                print(player.toons[i].name + "   HP: " + str(player.toons[i].HP))
        newWindow()
        for i in enemy.squad:
                print(enemy.toons[i].name + "   HP: " + str(enemy.toons[i].HP))
        newWindow()

def squadManage(): #currently working as intended 5/25/19
        newWindow()
        print("Current squad:", end=" ")
        print(player.squad)
        print("Available toons:", end=" ")
        print(player.toons_list)
        #selection index begins at 0 :D
        selection = input("Select a hero to add to your squad\
                 (type 'reset' to reset, 'end' when done)")
        if selection == "":
                print("Sorry, try again!")
                squadManage()
        elif selection == "reset":
                player.squad = []
                player.poptoons_list()
                squadManage()
        elif selection == "end":
                player.poptoons_list()
                mainMenu()
        elif int(selection) in range(len(player.toons_list)) and not player.toons_list[int(selection)] in player.squad:
                player.squad.append(player.toons_list.pop(int(selection)))
                squadManage()
        else:
                print("Sorry, try again!")
                squadManage()

def quitGame():
        newWindow()
        print("Goodbye!")
        exit()
def createPlayer():
        return Player(input("Type the name of your player! ")) # start a new game
def newWindow():
        print("-------------------")

game = Game()
enemy = EnemyPlayer()
player = createPlayer()
mainMenu()