import time

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
                self.HP = 100
                self.energy = 10
                self.attack = 10
                self.defense = 5
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

def mainMenu():
        print("Hero: "+current_player.name)
        print("Toons:", end=" ") 
        print(current_player.toons_list)
        print("Current Squad: "+str(current_player.squad))
        print("Options: fight squad quit\n")
        menu = input().lower()
        if menu == "fight":
                battle()
        elif menu == "squad":
                squadManage(current_player)
        elif menu == "quit":
                quitGame()
        else:
                print("Please select another option. \n")

def battle():
        print("Battles aren't ready yet, going back to main menu...")
        time.sleep(1)
        mainMenu()

def squadManage(Player):
        print ("Squad Manage isn't ready yet, going back to main menu...")
        time.sleep(1)
        mainMenu()

def quitGame():
        print("Goodbye!")
        exit()

current_player = createPlayer()
mainMenu()