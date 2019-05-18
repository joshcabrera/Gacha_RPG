import time, random


#Player clas
class Player:
        #method for populating the list of toons. 
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
                self.inventory = [] # undecided to attach items to characters or toons
                #self.currency = 0 # unused for now. unclear if collecting/spending currency is fun
                self.squad = [] # squad used for battles 
                self.poptoons_list() 
        

class EnemyPlayer:
        #TODO spawn monsters until there are [integer] unique monster names in the list
        def spawnMonsters(self, integer):
                for i in range(integer):
                        self.squad.append(random.choice(list(self.toons.values())).name)
        #clear the squad (after battles, for example)
        def clearSquad(self):
                self.squad = []
        #populate the squad list
        def popSquad(self):
                for i in self.toons.values():
                        self.squad.append(i)
        def __init__(self):
                self.toons = {
                        "George":Monster1("George") #dictionary of toons
                }
                #squad is a list of names of monsters. they must be the same as the keys in the
                #dictionary self.toons. the monster names must be unique 
                self.squad = []

#starting toon
class Bob:
        def __init__(self):
                self.name = "Bob"
                self.level = 1
                self.EXP = 0
                self.actions = ["Punch", "Kick"] # list of possible actions
                #self.status = [] #status effects
                self.items = [] # items; undecided to tie items to toons or characters
                self.HP_max = 100 #should be a multiple of level - should it 
                #be linear or exponential growth?
                self.HP = 100 # current HP
                self.energy_max = 10 #unused
                self.energy = 10 #unused
                self.attack_def = 10
                self.attack = 10 # see HP comment
                self.defense_def = 5
                self.defense = 5 # see HP comment - also, multiplier or flat reduction to damage received?
                self.speed_def = 100
                self.speed = 100 # unused - how to determine turn order?
        def punch(self): #how to differentiate between attacks?
                return self.attack
        def kick(self):
                return self.attack

class Monster1:
        def __init__(self, name):
                self.name = name
                self.level = 1
                self.EXP_drop = 50 # variable or constant?
                self.actions = ["Punch", "Kick"] # how to randomly select attacks? or do a pattern?
                self.status = []
                self.HP = 100 #randomize? #also, should there be an HPmax (for healing)
                self.energy = 10 #unused
                self.attack = 5
                self.defense = 3
                self.speed = 100
        def punch(self):
                return self.attack
        def kick(self):
                return self.attack

def mainMenu(): #main menu
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
        enemy.spawnMonsters(2) #spawns a number of monsters
        while current_player.squad and enemy.squad: #while both squads have toons in them
                print("Battle Round")
                battleRound()
        endBattle()

def endBattle(): #end the battle and clean up
        newWindow()
        print("Battle over!")
        enemy.squad = [] #empty the enemy squad (if the player loste)
        for i in current_player.squad: #heal everyone in the player's squad
                current_player.toons[i].HP = current_player.toons[i].HP_max
        mainMenu()

def battleRound():
        newWindow()
        if not current_player.squad or not enemy.squad: 
                endBattle()
        else:
                print(current_player.squad)
                print(enemy.squad)
                for i in current_player.squad:
                        print(i)
                        for j in range(len(current_player.toons[i].actions)):
                                print(current_player.toons[i].actions[j])

                choice = input()
                if choice == "1":
                        enemy.toons[enemy.squad[0]].HP -= current_player.toons[current_player.squad[0]].punch()
                        if enemy.toons[enemy.squad[0]].HP <= 0:
                                del enemy.squad[0]
                        battleRound()
                elif choice == "2":
                        enemy.toons[enemy.squad[0]].HP -= current_player.toons[current_player.squad[0]].kick()
                        if enemy.toons[enemy.squad[0]].HP <= 0:
                                del enemy.squad[0]
                        battleRound()
                elif choice == "run":
                        endBattle()
                else:
                        print("Sorry, please choose another option: ")
                        battleRound()

def squadManage(): #currently working as intended 5/18/19
        newWindow()
        print("Current squad:", end=" ")
        print(current_player.squad)
        print("Available toons:", end=" ")
        print(current_player.toons_list)
        #selection index begins at 0 :D
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
def createPlayer():
        return Player(input("Type the name of your player! ")) # start a new game
def newWindow(): #used to space out commands
        print("-------------------")

enemy = EnemyPlayer()
current_player = createPlayer()
mainMenu()