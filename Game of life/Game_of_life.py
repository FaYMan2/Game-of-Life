import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import userGrid
    

global image_3d
global image
rows : int = 20
cols : int = 20
color_map = {0 : np.array([255,255,255]),
             1 : np.array([0,0,0])
    }




def setup(inpt):
    
    if inpt == 'No':
        globals()['image'] = userGrid.drawGrid(grid_size=rows)
    elif inpt == 'Yes' or inpt == 'yes':
        globals()['image'] = np.random.rand(rows,cols) * 2
        globals()['image'] = np.floor(globals()['image'])
    
    
    print(globals()['image'].shape)
    globals()['image_3d'] = np.ndarray(shape = (rows,cols,3),dtype = int)
    
    for i in range(rows):
        for j in range(cols):
            globals()['image_3d'][i][j] = color_map[globals()['image'][i][j]]
            
            
def plot(img):
    plt.imshow(img)
    plt.axis('off')
    plt.show()    


def update():
    imgCopy = np.copy(globals()['image'])
    print(imgCopy)

    directions = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,0)]
    
    for i in range(rows):
        for j in range(cols):
            score = 0
            for dir in directions:
                ni = i + dir[0]
                nj = i + dir[1]
                
                if ni >= 0 and ni < rows and nj >=0 and nj < cols and globals()['image'][ni][nj] == 1:
                    score += 1
                    
            if score > 3 and globals()['image'][i][j] == 1:
                imgCopy[i][j] = 0
            
            elif score < 2 and globals()['image'][i][j] == 1:
                imgCopy[i][j] = 0
            
            elif score > 3 and globals()['image'][i][j] == 0:
                imgCopy[i][j] = 1
                
                
    globals()['image'] = np.copy(imgCopy)
    for i in range(0, image.shape[0]):
        for j in range(0, image.shape[1]):
            globals()['image_3d'][i][j] = color_map[imgCopy[i][j]]
    
def animate(x): 
    update()
    plt.cla()
    plot(globals()['image_3d'])




def run():
    fig = plt.figure(figsize = (30,30))
    ani = FuncAnimation(fig,animate,interval = 500)
    plt.show()



if __name__ == "__main__":
    userIpt = input('Random or not')
    setup(userIpt)
    run()