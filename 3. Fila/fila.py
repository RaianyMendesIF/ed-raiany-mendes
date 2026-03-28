class Node:
    def __init__(self, data=None, time = 0):
        self.data = data            
        self.next = None
        self.time = time 

class Queue:
    def __init__(self):
        self.head = None            
        self.tail = None  
        self._size = 0 

    # Insere
    def enqueue(self, elem, time):
            node = Node(elem, time)
            if self.tail is None:           
                self.tail = node            
                self.head = node                       
            else:
                self.tail.next = node       
                self.tail = node            
            self._size = self._size + 1
    
    # Remove
    def dequeue(self):
        if self._size > 0:
            elem  = self.head.data
            self.head = self.head.next
    
            if self.head is None:
                self.tail = None

            self._size -= 1
            return elem
        raise IndexError("A fila está vazia!")


    def show(self):
        pointer = self.head
        while pointer:
            print(f"({pointer.data} - {pointer.time})")
            pointer = pointer.next


    def quantum(self, quantum):
        while self.head:
            self.head.time = self.head.time - quantum
            if self.head.time <= 0:
                print(f"{self.head.data} removido! Tempo: {self.head.time}")
                self.dequeue()
            else:
                node = self.head.data
                time = self.head.time
                self.dequeue()
                self.enqueue(node, time)
            #self.show()
            #print()


## TESTANDO

fila = Queue()

fila.enqueue(1, 7)  # 3  | -1 | 
fila.enqueue(2, 10) # 6  | 2  | -2 | 
fila.enqueue(3, 15) # 11 | 7  | 3  | -1 |
fila.enqueue(4, 20) # 16 | 12 | 8  |  4 | 0 |
fila.enqueue(5, 9)  # 5  | 1  | -3 |

fila.show()

fila.quantum(4)

# Raiany Vitoria Prado Mendes  | TADS 3