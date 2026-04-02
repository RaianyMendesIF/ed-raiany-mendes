class Node:
    def __init__(self, data=None):
        self.data = data            # armazena o dado
        self.next = None            # referência para o próximo nó 
class Deque:
    def __init__(self):
        self.head = None            # indica a extremidade esquerda;
        self.tail = None            # indica a extremidade direita;
        self._size = 0              # armazena o número atual de elementos.

# Insere um elemento no início
    def add_start(self, elem):
        node = Node(elem)
        if self.head is None:           # Vazia
            self.tail = node            # Último nó da lista aponta para o novo nó 
            self.head = node            # Primeiro nó da lista aponta para o novo nó             
        else:
            node.next = self.head
            self.head = node
        self._size = self._size + 1
    
    # retorna itens da fila
    def show(self):
        pointer = self.head
        while pointer:
            print(pointer.data,end="")
            pointer = pointer.next

    def funcao(self):
            pointer = self.head
            prev = None
            i = 0
            print(f"{i} - pointer: {pointer.data} | prev:{prev}")
            while pointer:
                i += 1
                prev = pointer
                pointer = pointer.next
                if (pointer== None):
                    print(f"{i} - pointer: {pointer} | prev:{prev.data}")
                else:
                    print(f"{i} - pointer: {pointer.data} | prev:{prev.data}")

deque = Deque()
deque.add_start(5)
deque.add_start(2)
deque.add_start(7)
deque.add_start(4)
deque.add_start(8)


deque.funcao()
deque.show()