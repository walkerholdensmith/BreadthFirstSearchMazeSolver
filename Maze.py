class Maze:
    def __init__(self, size):
        self.maze = []
        #Creates a version of matrix from gui to be solved
        for i in range(size):
            subList = []
            for j in range(size):
                subList.append(' ')
            self.maze.append(subList)
        self.solutions = []

    #Returns maze
    def getMaze(self):
        return self.maze

    #Calls all other methods in class to run BFS algorithm
    def run(self, start, end, blocked):
        self.applyStart(start)
        self.applyEnd(end)
        min = len(self.maze) * len(self.maze)
        for block in blocked:
            self.applyBlocks(block)
        self.bfs(self,start,end)
        for path in self.solutions:
            if len(path) < min:
                min = len(path)
                shortest = path
        return shortest

    #Applys blocked positions to the matrix
    def applyBlocks(self, blocked):
        self.maze[int(blocked[1])][int(blocked[0])] = 'x'

    # Adds start position to board
    def applyStart(self, start):
        self.maze[int(start[1])][int(start[0])] = 'S'

    # Updated board to have end position
    def applyEnd(self, end):
        self.maze[int(end[1])][int(end[0])] = 'E'

    #Represents the matrix in the command line version of the application
    def representListOfList(self):
        count = 0
        print("    0    1    2    3    4 ")
        for list in self.maze:
            print(str(count) + " " + str(list))
            count += 1

    #Draws shortest path in command line version of application
    def drawShortest(self, shortrest):
        for step in shortrest:
            x = step[0]
            y = step[1]
            if (self.maze[y][x] != "S" and self.maze[y][x] != "E"):
                self.maze[y][x] = "*"

    #Breadth First Search algortim
    def bfs(self,graph, start, end):  # function for BFS
        visited = []
        queue = [[start]]
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node not in visited:
                neighbours = self.getNeighbours([], self.maze, node[0], node[1])
                for neighbour in neighbours:
                    if neighbour not in visited:
                        new_path = list(path)
                        new_path.append(neighbour)
                        queue.append(new_path)
                        if neighbour == end:
                            self.solutions.append(new_path)
                visited.append(node)

    #Searchs for neighbour nodes that can be traveled to, can travel diagonal just ununcomment lines 97-108
    def getNeighbours(self,neighbours, maze, x, y):
        (M, N) = (len(maze), len(maze[0]))
        # down
        if (y + 1 < M and [x, y + 1] and maze[y + 1][x] != "x"):
            neighbours.append([x, y + 1])
        # up
        if (y - 1 >= 0 and [x, y - 1] and maze[y - 1][x] != "x"):
            neighbours.append([x, y - 1])
        # right
        if (x + 1 < N and [x + 1, y] and maze[y][x + 1] != "x"):
            neighbours.append([x + 1, y])
        # left
        if (x - 1 >= 0 and [x - 1, y] and maze[y][x - 1] != "x"):
            neighbours.append([x - 1, y])
        '''
        Comment out the ability to check diagonal neighbors
        '''
        # # down right
        # if (x + 1 < N and y + 1 < M and [x + 1, y + 1] and maze[y + 1][x + 1] != "x"):
        #     neighbours.append([x + 1, y + 1])
        # # up left
        # if (x - 1 >= 0 and y - 1 >= 0 and [x - 1, y - 1] and maze[y - 1][x - 1] != "x"):
        #     neighbours.append([x - 1, y - 1])
        # # left up
        # if (x + 1 < N and y - 1 >= 0 and [x + 1, y - 1] and maze[y - 1][x + 1] != "x"):
        #     neighbours.append([x + 1, y - 1])
        # # left down
        # if (x - 1 >= 0 and y + 1 < M and [x - 1, y + 1] and maze[y + 1][x - 1] != "x"):
        #     neighbours.append([x - 1, y + 1])
        return neighbours

