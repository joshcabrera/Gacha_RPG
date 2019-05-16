import time, random

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
                self.inventory = []
                self.currency = 0
                self.squad = []
                self.poptoons_list()
        
class EnemyPlayer:
        def spawnMonsters(self, integer):
                for i in range(integer):
                        self.squad.append(random.choice(list(self.toons.values())))
        def clearSquad(self):
                self.squad = []
        def __init__(self):
                self.toons = {
                        "Monster1":Monster1("George")
                }
                self.squad = []
        
class Bob:
        def __init__(self):
                self.name = "Bob"
                self.level = 1
                self.EXP = 0
                self.actions = ["Punch", "Kick"]
                self.status = []
                self.items = []
                self.HP_max = 100
                self.HP = 100
                self.energy_max = 10
                self.energy = 10
                self.attack_def = 10
                self.attack = 10
                self.defense_def = 5
                self.defense = 5
                self.speed_def = 100
                self.speed = 100
        def punch():
                return attack
        def kick():
                return attack

class Monster1:
        def __init__(self, name):
                self.name = name
                self.level = 1
                self.EXP_drop = 50
                self.actions = ["Punch", "Kick"]
                self.status = []
                self.HP = 100
                self.energy = 10
                self.attack = 5
                self.defense = 3
                self.speed = 100
        def punch():
                return attack
        def kick():
                return attack

def createPlayer():
        return Player(input("Type the name of your player! "))

def newWindow():
        print("-------------------")

def mainMenu():
        newWindow()
        print("Hero: "+current_player.name)
        print("Toons:", end=" ") 
        print(current_player.toons_list)
        print("Current Squad: "+str(current_player.squad))
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

def startBattle():
        newWindow()
        enemySquad = spawnMonsters(2)
        while current_player.squad and enemySquad:
                print("Battle Round")
                battleRound()
        endBattle()

def endBattle():
        newWindow()
        print("Battle over!")
        enemySquad = []
        for i in current_player.squad:
                i.HP = i.HP_max
        mainMenu()

def battleRound():
        newWindow()
        # if not playerSquad or not enemySquad: 
        #         endBattle()
        # else:
        print(current_player.squad)
        print(enemySquad)
        for i in current_player.squad:
                print(i)
                for j in range(len(current_player.toons[i].actions)):
                        print(current_player.toons[i].actions[j])

        choice = input()
        if choice == "1":
                enemySquad[0].HP -= current_player.toons[current_player.squad[0]].punch()
                if enemySquad[0].HP <= 0:
                        del enemySquad[0]
                battleRound()
        elif choice == "2":
                enemySquad[0].HP -= current_player.toons[current_player.squad[0]].kick()
                if enemySquad[0].HP <= 0:
                        del enemySquad[0]
                battleRound()
        elif choice == "run":
                endBattle()
        else:
                print("Sorry, please choose another option: ")
                battleRound()

def squadManage():
        newWindow()
        print("Current squad:", end=" ")
        print(current_player.squad)
        print("Available toons:", end=" ")
        print(current_player.toons_list)

        selection = input("Select a hero to add to your squad\
                 (type 'reset' to reset, 'end' when done)")
        if selection == "reset":
                current_player.squad = []
                current_player.poptoons_list()
                squadManage()
        elif selection == "end":
                current_player.poptoons_list()
                mainMenu()
        elif int(selection) in range(len(current_player.toons_list)) and not current_player.toons_list[int(selection)] in current_player.squad:
                current_player.squad.append(current_player.toons_list.pop(int(selection)))
                squadManage()
        else:
                print("Sorry, try again!")
                squadManage()

def quitGame():
        newWindow()
        time.sleep(1)
        print("Goodbye!")
        exit()

enemy = EnemyPlayer()
current_player = createPlayer()
mainMenu()