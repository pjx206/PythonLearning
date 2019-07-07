import sys
import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


OFF = 0
ON = 255
vals = [ON, OFF]


def addGlider(i, j, grid):
    """adds a glider with top left cell at (i, j)"""
    glider = np.array([[0, 0, 255],
                       [255, 0, 255],
                       [0, 255, 255]])
    grid[i:i+3, j:j+3] = glider


def addGosper(i, j, grid, N):
    """Gosper Glider Gun in short: GGG"""
    if N >= 38:
        GGG = np.array([
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,ON,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,ON,0,ON,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,ON,ON,0,0,0,0,0,0,ON,ON,0,0,0,0,0,0,0,0,0,0,0,0,ON,ON,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,ON,0,0,0,ON,0,0,0,0,ON,ON,0,0,0,0,0,0,0,0,0,0,0,0,ON,ON,0],
            [0,ON,ON,0,0,0,0,0,0,0,0,ON,0,0,0,0,0,ON,0,0,0,ON,ON,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,ON,ON,0,0,0,0,0,0,0,0,ON,0,0,0,ON,0,ON,ON,0,0,0,0,ON,0,ON,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,ON,0,0,0,0,0,ON,0,0,0,0,0,0,0,ON,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,ON,0,0,0,ON,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,ON,ON,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        ])
        grid[i:i+11, j:j+38] = GGG
    else:
        print('No enough space for Gosper Glider Gun')
        grid = randomGrid(N)

def addPattern(i, j, grid, patternFile):
    #TODO:解决读取数据问题
    with open(patternFile, 'r', encoding='utf-8') as p:
        N = f.readline()
        grid = np.zeros((N, N))
        


        




def randomGrid(N):
    """return a gird of NxN random values"""
    return np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)


def update(frameNum, img, grid, N):
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            total = int((grid[i, (j-1) % N] + grid[i, (j+1) % N] +
                         grid[(i-1) % N, j] + grid[(i+1) % N, j] +
                         grid[(i-1) % N, (j-1) % N] + grid[(i-1) % N, (j+1) % N] +
                         grid[(i+1) % N, (j-1) % N] + grid[(i+1) % N, (j+1) % N])/255)
            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            elif total == 3:
                newGrid[i, j] = ON
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img


def main():
    parser = argparse.ArgumentParser(
        description='Runs Conway\'s Game of Life simulation')
    parser.add_argument('--grid-size', dest='N', required=False)
    parser.add_argument('--mov-file', dest='movfile', required=False)
    parser.add_argument('--interval', dest='interval', required=False)
    parser.add_argument('--add', dest='pattern', required=False)
    parser.add_argument('--pattern-file', dest='file',required = False)
    args = parser.parse_args()

    N = 100
    if args.N and int(args.N) > 8:
        N = int(args.N)

    updateInterval = 60
    if args.interval:
        updateInterval = int(args.interval)

    grid = np.array([])
    if args.pattern:
        if str(args.pattern) == 'Glider':
            grid = np.zeros(N*N).reshape(N, N)
            addGlider(1, 1, grid)
        elif str(args.pattern) == 'GGG':
            grid = np.zeros(N*N).reshape(N, N)
            addGosper(10, 10, grid, N)
    elif args.file:
        pfile = str(args.file)
        grid = np.zeros(N*N).reshape(N,N)
        addPattern(0, 0, grid, pfile)
    else:
        grid = randomGrid(N)

    fig, ax = plt.subplots()
    img = ax.imshow(grid)
    print('type of img: %s' % str(type(img)))
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N),
                                  frames=10,
                                  interval=updateInterval,
                                  save_count=50)

    if args.movfile:
        ani.save(args.movfile, fps=30, extra_args=['-vcodec', 'libx264'])
    plt.show()


if __name__ == '__main__':
    main()
