class NaivePriorityQueue():
        
    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority):
        if priority < 0:
            print("Error: priority cannot be lower than 0.")
            quit()
        tupleToAppend = (item, priority)
        self.queue.append(tupleToAppend)

    def is_empty(self):
        if len(self.queue) == 0:
            return(True)
        return(False)
    
    def dequeue(self):
        greatestPriority = self.queue[0][1]
        indexOfGreatestPriority = 0
        for i in range(len(self.queue)):
            if self.queue[i][1] < greatestPriority:
                greatestPriority = self.queue[i][1]
                indexOfGreatestPriority = i
        itemToReturn = self.queue[indexOfGreatestPriority]
        self.queue.remove(self.queue[indexOfGreatestPriority])
        return(itemToReturn) 