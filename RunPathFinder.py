
from Maze import Maze
from View import View

def main():
    size = int(input("how big of a matrix?: "))
    maze = Maze(size)
    view = View()
    view.runGame(maze,size)
if __name__ == '__main__':
    main()