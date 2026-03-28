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

    def isEmpty(self):
        if(self._size > 0):
            return False
        else:
            return True
    
    def validar_expressao(self, expressao):
        for i in expressao:
            if(i == "("):
                self.push("(")
            elif(i == ")"):
                if(self.isEmpty()):
                    return "Expressão inválida - Fechamento sem abertura"
                else:
                    self.pop()
        if(self.isEmpty()):
            return "Expressão válida"
        else:
            return "Expressão inválida - Abertura sem fechamento"

pilha = Stack()

expressao = input("EXPRESSÃO: ")

print(pilha.validar_expressao(expressao))