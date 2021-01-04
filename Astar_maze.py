import tkinter
window = tkinter.Tk()
window.title('maze')
window.geometry('300x330')

canvas=tkinter.Canvas(window,height=300,width=300)
canvas.place(x=0,y=0)

for i in range(1,30):
    canvas.create_line(0,10*i,300,10*i,fill="grey")
    canvas.create_line(10*i,0,10*i,300,fill="grey")    
canvas.create_line(0,300,300,300,fill="black")

dest=[3,1]
source=[5,28]
wall=[[5,0],[5,1],[5,2],[5,3],[5,4],
      [2,4],[3,4],[4,4],
      [10,0],[10,1],[10,2],[10,3],[10,4],[10,5],[10,6],[10,7],[10,8],[10,9],[10,10],[10,11],[10,12],[10,13],[10,14],
      [15,10],[15,11],[15,12],[15,13],[15,14],[15,15],[15,16],[15,17],[15,18],[15,19],[15,20],[15,21],[15,22],[15,23],
      [18,20],[19,20],[20,20],[21,20],[22,20],
      [18,21],[18,22],[18,23],[18,24],
      [0,24],[1,24],[2,24],[3,24],[4,24],[5,24],[6,24],[7,24],[8,24],[9,24],[10,24],[11,24],[12,24],[13,24],[14,24],[15,24],[16,24],[17,24]]

def drawSquare(coord,color):
    x=coord[0]
    y=coord[1]
    canvas.create_rectangle(x*10, y*10, x*10+10, y*10+10, fill=color)

drawSquare(source, "red")
drawSquare(dest, "lightgreen")

for brick in wall:
    drawSquare(brick, "black")

def extensions(current,currlength):
    last=current[-1]
    npaths=[]
    nlengths=[]
    if (last[0]>0) and ([last[0]-1,last[1]] not in current)and([last[0]-1,last[1]] not in wall):
        npaths.append(current+[[last[0]-1,last[1]]])
        nlengths.append(currlength+1)
    if (last[0]<29) and ([last[0]+1,last[1]] not in current)and ([last[0]+1,last[1]] not in wall):
        npaths.append(current+[[last[0]+1,last[1]]])
        nlengths.append(currlength+1)
    if (last[1]>0) and ([last[0],last[1]-1] not in current)and ([last[0],last[1]-1] not in wall):
        npaths.append(current+[[last[0],last[1]-1]])
        nlengths.append(currlength+1)
    if (last[1]<29) and ([last[0],last[1]+1] not in current)and ([last[0],last[1]+1] not in wall):
        npaths.append(current+[[last[0],last[1]+1]])
        nlengths.append(currlength+1)
    if (last[0]>0)and(last[1]>0)and([last[0]-1,last[1]-1]not in current)and([last[0]-1,last[1]-1]not in wall):
        npaths.append(current+[[last[0]-1,last[1]-1]])
        nlengths.append(currlength+1.41421)
    if (last[0]<29)and(last[1]<29)and([last[0]+1,last[1]+1]not in current)and([last[0]+1,last[1]+1]not in wall):
        npaths.append(current+[[last[0]+1,last[1]+1]])
        nlengths.append(currlength+1.41421)
    if (last[0]>0)and(last[1]<29)and([last[0]-1,last[1]+1]not in current)and([last[0]-1,last[1]+1]not in wall):
        npaths.append(current+[[last[0]-1,last[1]+1]])
        nlengths.append(currlength+1.41421)
    if (last[0]<29)and(last[1]>0)and([last[0]+1,last[1]-1]not in current)and([last[0]+1,last[1]-1]not in wall):
        npaths.append(current+[[last[0]+1,last[1]-1]])
        nlengths.append(currlength+1.41421)
    return npaths, nlengths

def arialDist(currentPos):
    return ( (currentPos[0]-dest[0])**2 + (currentPos[1]-dest[1])**2 )**0.5

def search():
    agenda = [ [source] ]
    exlist = []
    plengths=[0]
    while len(agenda)>0:
        best = plengths[0] + arialDist(agenda[0][-1])
        currindex = 0
        for i in range(1,len(agenda)):
            if (plengths[i] + arialDist(agenda[i][-1])) < best:
                best = plengths[i] + arialDist(agenda[i][-1])
                currindex = i
        current = agenda.pop(currindex)
        #drawSquare(current[-1], "cyan")
        currlength = plengths.pop(currindex)
        exlist += [current[-1]]
        if current[-1]==dest:
            return current
        npaths,nlengths = extensions(current,currlength)       
        agenda += npaths
        plengths += nlengths
        for p in agenda:
            if p[-1] in exlist:
                plengths.pop(agenda.index(p))
                agenda.remove(p)

def showpath():
    searchButton.configure(state="disabled")
    path = search()
    if path==None:
        print("no path found")
        return None
    path.pop(0)
    path.pop(-1)
    for step in path:
        drawSquare(step, "blue")

searchButton=tkinter.Button(window,text="search path",command=showpath)
searchButton.place(x=50,y=302)

window.mainloop()
