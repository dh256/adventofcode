import re        

class Graph:
    def __init__(self, nodes, numWorkers=5):
        self.graph = {}
        for asciiCode in range(65, 91):
            self.graph[chr(asciiCode)] = []
        
        # populate link nodes
        for node in nodes: 
            if node.pre in self.graph:
                self.graph[node.pre].append(node.post)
            
        # sort link nodes into descending alphabetical order
        for key,val in self.graph.items():
            val.sort()

        # visited nodes - initially empty
        self.visitedNodes = []

        # available nodes - initially those nodes with no predecessors
        self.initialiseAvailableNodes()
        
        # PART 2 - add workers
        self.workers = [Worker(workerId+1) for workerId in range(0,numWorkers)]

    def outputVisitedNodes(self):
        output = ''
        for node in self.visitedNodes:
            output = f'{output}{node}'
        return output

    def initialiseAvailableNodes(self):
        self.availableNodes = []
        for node in self.graph:
            predecessors = self.predecessors(node)
            if len(predecessors) == 0:
                self.availableNodes.append(node)
        self.availableNodes.sort()

    # list all the predecessors of given node i.e. all nodes that link to given node
    def predecessors(self, node):
        predecessors = []
        for key, val in self.graph.items():
            if node in val:
                predecessors.append(key)
        predecessors.sort()
        return predecessors

    def predecessorsAllVisited(self, node):
        # predecessors all visited if all preceeding nodes in visited nodes
        allVisited = True
        predecessors = self.predecessors(node)
        for predecessor in predecessors:
            if predecessor not in self.visitedNodes:
                allVisited = False
                break
        return allVisited
            
    def updateAvailableNodes(self, node):
        # update available nodes to:
        #  1. Include all successor nodes of given node
        #  2. Remove given node
        # Available nodes must not contain duplicated and must always be sorted in alphabetical order
        newAvailableNodes = self.graph[node]
        for newAvailableNode in newAvailableNodes:
            if not newAvailableNode in self.availableNodes:
                self.availableNodes.append(newAvailableNode)
        if node in self.availableNodes:
            self.availableNodes.remove(node)
        self.availableNodes.sort()

    def stepOrder(self):
        # while there are available nodes:
        #  check each available node in order. 
        #  First node where all predecessors have been visited should be added to visited nodes
        #  Available nods are then updated to include all successors of just visited node (do not allow duplicates to be added to available nodes) and remove just visited node
        #  Note: Available nodes must remain in alphabetical order 
        #  Break and repeat
        self.visitedNodes = []
        self.initialiseAvailableNodes()
        while len(self.availableNodes) > 0:
            for node in self.availableNodes:
                if self.predecessorsAllVisited(node):
                    self.visitedNodes.append(node)
                    self.updateAvailableNodes(node)
                    break            
    
    def starters(self, currentTime):
        # get all available nodes and workers
        # assign available nodes to available workers
        availableWorkers = [worker for worker in self.workers if worker.available()]
        availableNodesWithPre = [node for node in self.availableNodes if self.predecessorsAllVisited(node)]
        availableWorkerIndex = len(availableWorkers) - 1
        for currNode in availableNodesWithPre:
            if availableWorkerIndex >= 0:
                avWorker = availableWorkers[availableWorkerIndex]
                avWorker.workingOn = currNode
                avWorker.finishTime = currentTime + (ord(currNode) - ord('A') + 1) + 60
                self.availableNodes.remove(currNode)
                availableWorkerIndex -= 1

    def finishers(self, currentTime):
        # any workers finishing at currentTime?
        for worker in self.workers:
            if worker.finishTime == currentTime:
                node = worker.workingOn
                worker.workingOn = None
                worker.finishTime = None
                self.visitedNodes.append(node)
                self.updateAvailableNodes(node)
    
    def workersAllAvailable(self):
       return len([worker for worker in self.workers if worker.available()]) == len(self.workers)

    def timeToCompleteSteps(self):
        # Part 2
        currentTime = 1
        self.visitedNodes = []
        self.initialiseAvailableNodes()
        complete = False
        while not complete:
            self.finishers(currentTime)
            
            # check if complete
            if len(self.availableNodes) == 0:
                complete = self.workersAllAvailable()
            
            if not complete:
                self.starters(currentTime)
                currentTime += 1

        return currentTime-1 

class Worker:
    def __init__(self,workerId):
        self.workerId = workerId
        self.workingOn = None
        self.finishTime = None

    def available(self):
        return self.workingOn == None

    def unavailable(self):
        return not self.available()    
    
class Node:
    def __init__(self, pre, post):
        self.pre = pre
        self.post = post

def processFile(filename):
    with open(filename, "r") as input:
        nodes = [Node(line.strip()[5], line.strip()[-12]) for line in input]
        return nodes

# solve puzzle
nodes = processFile("day7.txt")
graph = Graph(nodes)

# Part 1 - Work out order in which steps should be completed
graph.stepOrder()
print(f'Step Order: {graph.outputVisitedNodes()}')

# Part 2 - Time to complete all steps
# 5 workers available each step takes 60 seconds plus number of seconds corresponding to its letter A=1 (61), B=2 (62), .. Z=26 (86) 
# Available steps can begin simultaneously but where multiple steps are available they must still begin alphabetically
time = graph.timeToCompleteSteps()
print(f'Time to complete steps: {time} seconds. Step order: {graph.outputVisitedNodes()}')
