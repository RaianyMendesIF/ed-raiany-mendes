class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkList:

    def __init__(self):
        self.head = None
        self._size = 0

    # Adicionar item na lisat
    def append(self, elem):
        if self.head:                   
            pointer = self.head         
            while(pointer.next):        
                pointer = pointer.next
            pointer.next = Node(elem)   
        else:
            self.head = Node(elem)      
        self._size = self._size + 1
    
    # Retornar o tamanho da lista
    def __len__(self):
        return self._size
    
    # Mostrar um item da lista
    def __getitem__(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")   
        if pointer:
            return pointer.data
        else:
            raise IndexError("list index out of range") 

    # Editar um item da lista   
    def __setitem__(self, index, elem):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")   
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("list index out of range") 

    ### ------ Sem sobrecarga ------

    # Inserir elemento no início da lista
    def insert_beginning(self, elem):
        pointer = self.head
        self.head = Node(elem)
        self.head.next = pointer
        self._size = self._size + 1
    
    # Inserir elemento no final da lista -- tale
    def insert_end(self, elem):
        pointer = self.head
        if pointer:
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            self.head = Node(elem)
        self._size = self._size + 1

    # Remover um elemento da lista
    def remove(self, value):
        pointer = self.head
        if pointer:
            if pointer.data == value:
                self.head = pointer.next
            else:
                while(pointer.next):
                    new_pointer = pointer.next
                    if new_pointer.data == value:
                        pointer.next = new_pointer.next
                        self._size = self._size - 1
                        return
                    else:
                        pointer = new_pointer
                raise ValueError(f"Valor {value} não encontrado na lista")
        else:
           raise ValueError("A lista está vazia")

    # Buscar um elemento na lista 
    def search(self, value):
        pointer = self.head
        i = 0
        if pointer:
            if pointer.data == value:
                return i
            else:
                while(pointer.next):
                    pointer = pointer.next
                    i += 1
                    if pointer.data == value:
                        return i
                   
                raise ValueError(f"Valor {value} não encontrado na lista")
        else:
           raise ValueError("A lista está vazia")


    # Imprimir os elementos da lista
    def print_list(self):
        nodes = []
        pointer = self.head
        if pointer:
            while(pointer):
                nodes.append(pointer.data)
                pointer = pointer.next
            for i in nodes:
                print(i, end=" -> ")
            print()
        else:
            raise ValueError("A lista está vazia")


    # Retornar o tamanho da lista
    def size(self):
        return self._size

    # Verificar se a lista está vazia
    def is_empty(self):
        pointer = self.head
        if pointer:
            return None
        else:
            return True 







## Teste

lista = LinkList()

lista.append(3)
lista.append(5)
lista.append(6)

print("Tamanho da lista:", len(lista))

print("Item de index 2 da lista", lista[2])

lista[2] = 10
print("Novo Item de index 2 da lista", lista[2])


lista.insert_beginning(20)

lista.insert_end(10)

print("posição do 20: ", lista.search(20))

lista.print_list()

print(lista.size())

if lista.is_empty():
    print("Lista está vazia")
else:
    print("Lista não está vazia")