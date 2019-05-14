import time, random

#PlayerObject
class Player:
        def poptoons_list(self):
                for toon in self.toons:
                        self.toons_list.append(toon.name)
        def __init__(self, name):
                self.name = name
                self.toons = [Bob()]
                self.toons_list = []
                self.inventory = []
                self.currency = 0
                self.squad = []
                self.state = "menu" #could be battle or squad
                self.menu = "menu" #could fight, squad, or quit
                self.poptoons_list()
        

#Starter Toon
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
        playerSquad = current_player.squad
        enemySquad = spawnMonsters(2)
        while playerSquad and enemySquad:
                battleRound()
        endBattle()

def endBattle():
        newWindow()
        print("Battle over!")
        enemySquad = []
        for i in playerSquad:
                i.HP = i.HP_max
        mainMenu()

def battleRound():
        newWindow()
        if not playerSquad or not enemySquad:
                print("Battle over!")
        print(playerSquad)
        print(enemySquad)
        print("Choose an option: \n (1) "+playerSquad[0].actions[0]+ " \
                (2) "+playerSquad[0].actions[1]) # TODO switch this to a loop
        print("(3) Run")

        choice = input()
        if choice == "1":
                enemySquad[0].HP -= playerSquad.punch()
                if enemySquad[0].HP <= 0:
                        del enemySquad[0]
                battleRound()
        elif choice == "2":
                enemySquad[0].HP -= playerSquad.kick()
                if enemySquad[0].HP <= 0:
                        del enemySquad[0]
                battleRound()
        elif choice == "3":
                endBattle()
        else:
                print("Sorry, please choose another option: ")
                battleRound()

def spawnMonsters(integer):
        enemySquad = []
        for i in range(integer):
                enemySquad.append(Monster1("Tester"))
        return enemySquad

def squadManage(): #TODO switch these lists to dictionaries.
        newWindow()
        print("Current squad:", end=" ")
        print(current_player.squad)
        print("Available toons:", end=" ")
        print(current_player.toons_list)    
        selection = input("Select a hero to add to your squad (type 'reset' to reset, 'end' when done)")
        if selection == "0":
                current_player.squad = []
                squadManage()
        elif selection == "end":
                current_player.poptoons_list()
                mainMenu()
        elif type(selection == int) and selection in range(len(current_player.toons_list)):
                current_player.squad.append(current_player.toons_list.pop([int(selection)]))
        else:
                print("Sorry, try again!")
        mainMenu()

def quitGame():
        newWindow()
        time.sleep(1)
        print("Goodbye!")
        exit()

playerSquad = []
enemySquad = []
current_player = createPlayer()
mainMenu()