import time, random

class Player:
        def poptoons_list(self):
                self.toons_list = []
                for name,toon in self.toons.items():
                        self.toons_list.append(toon.name)
        def __init__(self, name):
                self.name = name      # character name
                self.toons = {        # dictionary containing toon objects
                        "Bob":Bob() #starting character
                }
                self.toons_list = [] # listen of toons currently owned
                self.inventory = [] # unused
                self.currency = 0 # unused for now. unclear if collecting/spending currency is fun
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
        def popSquad(self):
                for i in self.toons.values():
                        self.squad.append(i)
        def fight(self):
                fighter_name = random.choice(list(self.toons.values())).name
                action = random.randrange(0, len(self.toons[fighter_name].actions))
                if action == 0:
                        print("Enemy punch!")
                        time.sleep(1)
                        return self.toons[fighter_name].punch()
                elif action == 1:
                        print("Enemy kick!")
                        time.sleep(1)
                        return self.toons[fighter_name].kick()
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
                self.actions = ["Punch", "Kick"] # list of possible actions
                #self.status = [] #status effects
                self.items = [] # items; undecided to tie items to toons or characters
                self.HP = 100
                self.HP_max = self.HP
                self.energy_max = 10 #unused
                self.energy = 10 #unused
                self.attack_def = 10
                self.attack = 12 
                self.defense_def = 5
                self.defense = 5 #multiplier or flat reduction to damage received?
                self.speed_def = 100
                self.speed = 100 # unused - how to determine turn order?
        def punch(self): 
                return (self.attack + random.randrange(-2, 2))
        def kick(self):
                return (self.attack + random.randrange(-3, 3))

class Monster1:
        def __init__(self, name):
                self.name = name
                self.level = 1
                self.EXP_drop = 50 # variable or constant?
                self.actions = ["Punch", "Kick"] # how to randomly select attacks? or do a pattern?
                self.status = []
                self.HP = 100
                self.HP_max = self.HP
                self.energy = 10 #unused
                self.attack = 4
                self.defense = 3
                self.speed = 100
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
        print("Options: fight squad quit\n")
        menu = input().lower()
        if menu == "fight":
                startBattle()
        elif menu == "squad":
                squadManage()
        elif menu == "quit":
                quitGame()
        else:
                print("Please select another option.")
                mainMenu()

def startBattle(): # TODO make this flow cleaner
        newWindow()
        enemy.spawnMonsters(2) #spawns 2 monsters for testing
        while player.squad and enemy.squad:
                battleRound()
        endBattle()

def endBattle():
        newWindow()
        print("Battle over!")
        enemy.clearSquad()
        for i in player.squad:
                player.toons[i].HP = player.toons[i].HP_max
        for i in enemy.toons.values():
                i.HP = i.HP_max
        mainMenu()

def battleRound():
        newWindow()
        if not player.squad or not enemy.squad: 
                endBattle()
        else:
                for i in player.squad:
                        print(player.toons[i].name + "   HP: " + str(player.toons[i].HP))
                        print("Actions:")
                        for j in range(len(player.toons[i].actions)):
                                print(player.toons[i].actions[j], end=" ")
                print("")
                newWindow()
                for i in enemy.squad:
                        print(enemy.toons[i].name + "   HP: " + str(enemy.toons[i].HP))
                choice = input()
                if choice == "1":
                        print(player.squad[0]+" punch!")
                        time.sleep(1)
                        enemy.toons[enemy.squad[0]].HP -= player.toons[player.squad[0]].punch()
                        if enemy.toons[enemy.squad[0]].HP <= 0:
                                del enemy.squad[0]
                        if enemy.squad:
                                player.toons[player.squad[0]].HP -= enemy.fight()
                                if player.toons[player.squad[0]].HP <= 0:
                                        del player.squad[0]
                        battleRound()
                elif choice == "2":
                        print(player.squad[0]+" kick!")
                        time.sleep(1)
                        enemy.toons[enemy.squad[0]].HP -= player.toons[player.squad[0]].kick()
                        if enemy.toons[enemy.squad[0]].HP <= 0:
                                del enemy.squad[0]
                        if enemy.squad:
                                player.toons[player.squad[0]].HP -= enemy.fight()
                                if player.toons[player.squad[0]].HP <= 0:
                                        del player.squad[0]
                        battleRound()
                elif choice == "wait":
                        player.toons[player.squad[0]].HP -= enemy.fight()
                        if player.toons[player.squad[0]].HP <= 0:
                                del player.squad[0]
                        battleRound()
                elif choice == "run":
                        print("Running away...")
                        time.sleep(2)
                        endBattle()
                else:
                        print("Sorry, please choose another option: ")
                        battleRound()

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

enemy = EnemyPlayer()
player = createPlayer()
mainMenu()