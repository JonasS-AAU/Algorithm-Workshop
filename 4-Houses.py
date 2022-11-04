from cmath import sqrt
import matplotlib.pyplot as plt
import random
import heapq

#Central service station (CSS)
hx = [500]
hy = [500]

Vertices = []
Vdist = []

#City constructor | That upholds the layout restrictions
def HouseConstructor(houses, area, mindist):
    for x in range(houses):
        fail = 1
        while fail == 1:
            xr = random.randint(0,area)
            yr = random.randint(0,area)
            mdist = sqrt(pow(xr-hx[0], 2) + pow(yr-hy[0],2)) #Længde til midten

            for j in range(len(hx)):
                ndist = sqrt(pow(xr-hx[j], 2) + pow(yr-hy[j],2))
                if 0 <= ndist.real <= mindist or 0 >= ndist.real >= -mindist:
                    fail = 1
                elif 0 <= mdist.real <= 10 or 0 >= mdist.real >= -10:
                    fail = 1
                else:
                    fail = 0
                    
            if fail != 1:
                hx.append(xr)
                hy.append(yr)
                fail = 0

    for i in range(len(hx)):
        tempV = []
        tempV.append(hx[i])
        tempV.append(hy[i])
        Vertices.append(tempV)
    #print("List of Vertices: ", Vertices)
    
    #List of distance From Vertice X to all other Vertices
    for i in range(len(hx)): 
        tempdist = []
        for j in range(len(hx)):
            tempVdist = sqrt(pow(hx[i]-hx[j], 2) + pow(hy[i]-hy[j],2))
            tempdist.append(tempVdist.real)
        #print(tempdist)
        Vdist.append(tempdist)
    #print("List of Vertice distances: ", Vdist)

    print("done with constructing")

class Prims:

    def __init__(self, vertices, distances) -> None:
        node = []
        self.MST = []
        self.minheap = []
        for x in range(len(vertices)): #Initializing the minheap to contain all vertices, with key = dist to root node
            node = [distances[0][x],x,0]
            self.minheap.append(node)
        heapq.heapify(self.minheap) #Enforcing minheap rules

    def SearchMST(self):
        while len(self.minheap) != 0: #While the minheap still contains nodes
            u = heapq.heappop(self.minheap) #Pop them, and add them to mst
            self.MST.append(u)
            
            for x in self.minheap: #ikke helt sikker på dette virker, ideen er check min heap igennem (vi kender at de alle er connected)
                if Vdist[u[1]][x[1]] < x[0]: #Hvis distancen u-v er mindre end key for v
                    #print("node: ", u[1])
                    #print("dist to be set: ", Vdist[u[1]][x[1]], "_ dist already existing: ", x[0])

                    x[0] = Vdist[u[1]][x[1]] #Uhm which one is it? think its this one?
                    #Vdist[u[1]][x[1]] = x[0] #Sæt den nye mindste distance som key for v
                    x[2] = u[1]
                    

            heapq.heapify(self.minheap) #Enforcing minheap rules
            #print("popped", u)
    
    def printMST(self):
        print("Final MST = ", self.MST)

    def printminheap(self): #Purely for testing purposes
        for x in self.minheap:
            print(":",x)

    def graphConstruct(self): #VIRKER IKKE, HAR BRUG FOR AT FINDE EN VEJ GENNEM TRÆET
        
        for i in range(len(self.MST)):
            x = []
            y = []
            #x.append(Vertices[self.MST[i][1]][0])
            #y.append(Vertices[self.MST[i][1]][1])
            x.append(Vertices[self.MST[i][2]][0])
            x.append(Vertices[self.MST[i][1]][0])
            y.append(Vertices[self.MST[i][2]][1])
            y.append(Vertices[self.MST[i][1]][1])
            #print("plotting:", self.MST[i][2], "and:", self.MST[i][1])
            plt.plot(x,y)

#Construct "city"
HouseConstructor(1000, 1000, 5)

p = Prims(Vertices, Vdist)

#p.printminheap()

p.SearchMST()

#p.printMST()

p.graphConstruct()

#Graphics plot

plt.scatter(hx,hy)
plt.xlim([0,1000])
plt.ylim([0,1000])
plt.show()