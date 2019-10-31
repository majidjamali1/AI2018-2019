import tkinter as tk


walls = []
buttons = []

root = tk.Tk()
solveAlgRoot = ""



class Queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def enQueue(self, item):
        self.items.insert(0, item)
    
    def deQueue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
 

def IDS():
    pass


def DFS():
    pass


def findMoves(row, col):

    moves =  []

    # we start from 0 and end in size-1

    if row < size - 1:
        # move right
        right = [row + 1, col]
        if right not in walls:
            moves.append(right)
    
    if row > 0:
        # move left
        left = [row - 1, col]
        if left not in walls:
            moves.append(left)
    
    if col < size - 1:
        # move down
        down = [row, col + 1]
        if down not in walls:
            moves.append(down)
    
    if col > 0:
        # move up
        up = [row, col - 1]
        if up not in walls:
            moves.append(up)

    return moves


def defineTreeStructure():
    tree = []
    for btn in buttons:
        nums = str.split(btn['title'], ", ")
        current = [int(nums[0]), int(nums[1])]
        if current not in walls:
            moves = findMoves(current[0], current[1])
            tree.append([current, moves])
    
    return tree


def findRoad(tree, road, end):

    start = [0, 0]

    for i in range(0, len(tree)):
        
        if tree[i][0] == end:
            road.append(end)
            for j in tree[i][1]:
                if j != start:
                    return findRoad(tree[0: i], road, j)
                else:
                    return road


def BFS():

    tree = defineTreeStructure()
    seen = []
    q = Queue()

    road = findRoad(tree, [], [size - 1, size - 1])
    print(road)


    



def saveRoadMap():

    f = open("roadMap.txt", "w+")

    for wall in walls:
        widgetName = "{}, {}".format(wall[0], wall[1])
        f.write(widgetName + "\n")

    f.close()


def showSolveAlgorithms(size):
    
    saveRoadMap()

    solveAlgRoot = tk.Tk()

    button1 = tk.Button(solveAlgRoot, text="BFS", name="bfs", command=BFS)
    button1.grid(row=2, column=1, sticky="nsew")

    # button2 = tk.Button(solveAlgRoot, text="DFS", name="dfs", command=DFS)
    # button2.grid(row=2, column=3, sticky="nsew")
    
    # button3 = tk.Button(solveAlgRoot, text="IDS", name="ids", command=IDS)
    # button3.grid(row=3, column=2, sticky="nsew")

    solveAlgRoot.grid_rowconfigure(1, weight=1)
    solveAlgRoot.grid_columnconfigure(1, weight=1)

    solveAlgRoot.title("select Algorithm")

    solveAlgRoot.geometry("200x200")

    solveAlgRoot.resizable(0, 0)

    solveAlgRoot.mainloop()

def setHereWall(row, col):
    widgetName = "{}, {}".format(row, col)

    if (row == 0 and col ==0) or (row == size-1 and col == size-1):
        # this is start point or end point! Then
        return

    if [row, col] not in walls:
        walls.append([row, col])
        for i in buttons:
            if i['title'] == widgetName:
                i['button']['bg'] = 'black'
                i['button']['fg'] = 'white'
                
    else:
        walls.remove([row, col])
        for i in buttons:
            if i['title'] == widgetName:
                i['button']['bg'] = 'white'
                i['button']['fg'] = 'black'
                
            

def createArea(size):

    for row in range(0, size):
        for col in range(0, size):
            buttonText = str()
            buttonText = "{}, {}".format(row, col)
            button = tk.Button(root, text=buttonText, name=buttonText, fg='black', 
                               command=lambda row=row, col=col: setHereWall(row, col))
            button.grid(row=row, column=col, sticky="nsew")
            buttons.append({"button": button, "title": buttonText})

    file = open("roadMap.txt", "r")
    line = file.readline()
    while line != "":

        nums = str.split(line, ", ")
        setHereWall(int(nums[0]), int(nums[1]))

        line = file.readline()

    nextStepButton = tk.Button(root, text = "Solve!", name="solvation", command=lambda row=size+2, col=0: showSolveAlgorithms(size))
    nextStepButton.grid(row=size+2, column=0, sticky="nsew")

    root.grid_rowconfigure(size, weight=2)
    root.grid_columnconfigure(size, weight=2)

    root.resizable(False, False)

    root.title("Set Walls Position")

    root.mainloop()

def setSize():

    size = input("enter size of maze: (non number for default size)")

    try:
        size = int(size)
        return size
    except:
        return 10



if __name__ == "__main__":
    size = setSize()
    createArea(size)
