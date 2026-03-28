class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.topo = None
        self._size = 0

    def push(self, data):
        new_node = Node(data)       
        new_node.next = self.topo   
        self.topo = new_node        
        self._size = self._size + 1

    def pop(self):
        if self.topo is None:
            return None
        removed = self.topo
        self.topo = self.topo.next
        self._size = self._size - 1
        return removed.data
    
    def __len__(self):
        return self._size
    
    def inverter(self, word):
        for i in word:
            self.push(i)

        while(len(self) > 0):
            print(self.pop(), end="")

pilha = Stack()

palavra = input("ENTRADA: ")

pilha.inverter(palavra)




