# Problem Solving with Algorithms and Data Structure
# http://interactivepython.org/courselib/static/pythonds/BasicDS/stacks.html
# Matthew Bodenstein
class Stack():
    ''' Implementation of an abstract data type/structure Stack,
        using physical implementation of a list data type.'''
    count = 0   # creates count variable
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def name(self):
        return str(self.name)

################## VARIABLES AND STACKS ###################
main = False
while main == False: # makes user pick a number 3-10
    try:
        num = int(input("Enter amount of disks between 3-10: "))
        if num >= 3 and num <= 10:
            main = True
        else: print("Try Again")
    except: print("Try Again")
towerA,towerB,towerC, total = Stack(),Stack(),Stack(), Stack()          # Creates the towers and the counting stack/variable
towers = [towerA,towerB,towerC]                                         # creates the 3 towers
for i in range(0,3):    towers[i].name =(input("Input Tower Names: "))  # user picks the player names
for i in range(num,0,-1):   towerA.push(i)                              # loads up the first tower
################## FUNCTIONS ###############
def printing(tower):
    for i in tower.items:
        print(i, end=' ')
    print()
def printing2():  # prints the towers and items in the towers
    print(towerA.name + ':\t', end=''), printing(towerA)
    print(towerB.name + ':\t', end=''), printing(towerB)
    print(towerC.name + ':\t', end=''), printing(towerC)
def move_disk(num, a, c, b):
    if num == 1:
        total.count += 1
        print('\n'+"< MOVE", str(total.count), '>\n' +a.name, " ------> ", c.name)
        c.push(a.pop())
        printing2()
        return total.count
    move_disk(num - 1, a, b, c)
    total.count += 1
    print('\n'+"< MOVE", str(total.count), '>\n' +a.name, " ------> ", c.name)
    c.push(a.pop())
    printing2()
    return move_disk(num - 1, b, c, a), total.count
################### MAIN CODE #########################
print("-------------GAME START-------------")
move_disk(num, towerA, towerC,towerB)
print("-------------GAME OVER-------------")