class Node:
    def __init__(self, id, position, parent=None, cost=0, depth=0):
        self.id = id
        self.position = position
        self.parent = parent
        self.cost = cost
        self.depth = depth
