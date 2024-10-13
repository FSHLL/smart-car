class Node:
    def __init__(self, id, position, parent=None, cost=0):
        self.id = id
        self.position = position
        self.parent = parent
        self.cost = cost

    # def add_child(self, child_node):
    #     self.children.append(child_node)
    #     child_node.parent = self
