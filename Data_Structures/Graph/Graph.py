from .NodeGraph import NodeGraph
from .Traveler import Traveler
from .QuickSort import QuickSort

class Graph:
    
    
    @staticmethod
    def connect(origin, target, weight=1, mutual=False, returnWeight=None):
        if isinstance(origin, NodeGraph) and isinstance(target, NodeGraph):
            origin.connections.append({target:weight})
            if mutual:
                target.connections.append({origin:returnWeight if returnWeight else weight})
        else:
            print("Connecting nodes must be NodeGraph instances.")
        return None
    
    def __init__(self):
        self.registeredNodes = []
        
    def registerNode(self, data):
        newNode = NodeGraph(data)
        self.registeredNodes.append(newNode)
        return newNode
    
    def deepSearch(self, origin, destiny, first=True, deepTraveler=None, res=None):
        if first:
            deepTraveler = Traveler()
            deepTraveler.setPosition(origin)
        if deepTraveler.currentPosition == destiny:
            res = deepTraveler.path
        # print(res)
        if res:
            return res
        for place in deepTraveler.getMapNodeOnly():
            if place in deepTraveler.path:
                continue
            placeIndex = deepTraveler.getMapNodeOnly().index(place)
            deepTraveler.travelTo(placeIndex)
            res = self.deepSearch(origin, destiny, False, deepTraveler, res)
            if res:
                return res
            deepTraveler.back()
        return res
    
    def deepSearchAll(self, origin, destiny, first=True, deepTraveler=None, res=[]):
        if first:
            deepTraveler = Traveler()
            deepTraveler.setPosition(origin)
        if deepTraveler.currentPosition == destiny:
            res.append(
                    {
                        "path":deepTraveler.getPathValueList(),
                        "cost":deepTraveler.travelTotalCost
                    }
                )
        for place in deepTraveler.getMapNodeOnly():
            if place in deepTraveler.path:
                continue
            print(deepTraveler)
            deepTraveler.showMap()
            
            placeIndex = deepTraveler.getMapNodeOnly().index(place)
            deepTraveler.travelTo(placeIndex)
            self.deepSearchAll(origin, destiny, False, deepTraveler, res)
            deepTraveler.back()
        if first:
            return res
    
    def getNodeByValue(self, value):
        for node in self.registeredNodes:
            if node.data == value:
                return node
        return None
    
    def breadthGenerateTree(self, origin, first=True, visitingQueue=[], visited=[], generateTree=None):
        print("Visiting: ", visitingQueue)
        print("Visited: ", visited)
        
        if first:
            generateTree = Graph()
            visitingQueue.append(origin)
        aux = QuickSort(origin.getConnectionNodesDict(), 1, "data").sorted
        connections = []
        for v in aux:
            connections.append(v["node"]) # Prioridade em ordem alfabética
            
        for connection in connections:
            if connection in visited:
                continue
            visitingQueue.append(connection)
        visited.append(origin)
        visitingQueue.pop()
        for node in visitingQueue:
            if node in visited:
                continue
            self.breadthGenerateTree(node, False, visitingQueue, visited, generateTree)
        if first:
            return visited
        
    def BFS(self, s): # Func to print BFS graph
        visited = [False] * (len(self.registeredNodes)) # Mark all verices as not visited

        queue = [] # Queue for BFS

        queue.append(s)
        visited[self.registeredNodes.index(s)] = True

        while queue:
            # Dequeue a vertice from queue and print it
            s = queue.pop(0)
            print(s, end=' ')

            # Get all adjacent vertices of dequeued vertex s
            # If an adjacent has not been visited, mark it visited and enqueue it
            for i in self.registeredNodes[self.registeredNodes.index(s)]:
                if visited[self.registeredNodes.index(i)] == False:
                    queue.append(i)
                    visited[self.registeredNodes.index(i)] = True
        
        
    
    
    
    @staticmethod
    def autofill(graph):
        a = graph.registerNode("a")
        b = graph.registerNode("b")
        c = graph.registerNode("c")
        d = graph.registerNode("d")
        e = graph.registerNode("e")
        f = graph.registerNode("f")
        g = graph.registerNode("g")
        h = graph.registerNode("h")
        graph.connect(a, b)
        graph.connect(a, e)
        graph.connect(a, f)
        graph.connect(b, c)
        graph.connect(b, e)
        graph.connect(c, d)
        graph.connect(e, d)
        graph.connect(e, g)
        graph.connect(f, e)
        graph.connect(f, h)
        graph.connect(g, c)
        graph.connect(g, h)
        graph.connect(h, d)
