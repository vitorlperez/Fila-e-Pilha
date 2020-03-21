#Adicionando um comentario de novo
class ArrayStack:
    def __init__(self):
        self._data = []
    def __len__(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data) == 0
    def push(self, e):
        self._data.append(e)
    def top(self):
        return self._data[-1]
    def pop(self):
        return self._data.pop()

class ArrayQueue:
    def __init__(self):
        self._data = []
        self._size = 0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size == 0
    def first(self):
        return self._data[0]
    def dequeue(self):
        self._data.pop(0)
        self._size -= 1
        return None
    def enqueue(self, e):
        self._data.append(e)
        self._size += 1

def find(list1, valuer):
    return list1.index(valuer)

n = input()
list = []
for i in range (int(n)):
    aux = input(str())
    list.append(aux.split())

is_fila = True
is_pilha = True

COD_ESQ = []
COD_DIR = []
for i in range(int(n)):
    x = list[i][0]
    COD_ESQ.append(x)
    y = list[i][3]
    COD_DIR.append(y)
list_soma = COD_ESQ + COD_DIR
list_soma.sort()
j = 0
while j < (len(list_soma)-1):
    if (list_soma[j] == list_soma[j+1]):
        list_soma.pop(j)
        list_soma.pop(j)
    else:
        j += 1


fila = ArrayQueue()
pilha = ArrayStack()
if (len(list_soma)!= 2):
    is_pilha = False
    is_fila = False
else:        
    for i in range(len(list_soma)):
        if list_soma[i] in COD_ESQ:
            x1 = list_soma[i]
        if list_soma[i] in COD_DIR:
            y2 = list_soma[i]
    inicial = COD_ESQ.index(x1)
    final = COD_DIR.index(y2)
    posicao = inicial
    while True:
        if list[posicao][1] == "PUSH":
            aux = list[posicao][2]
            fila.enqueue(aux)
            pilha.push(aux)
        if list[posicao][1] == "POP":
            if pilha.is_empty():
                is_pilha = False
            else:
                if pilha.top() == list[posicao][2]:
                    pilha.pop()
                else:
                    is_pilha = False
            if fila.is_empty():
                is_fila = False
            else:
                if fila.first() == list[posicao][2]:
                    fila.dequeue()
                else:
                    is_fila = False
        if posicao == final:
            if not pilha.is_empty:
                is_pilha = False
            if not fila.is_empty:
                is_fila = False
            break
        if (is_pilha == False) and (is_fila == False):
            print("nenhuma")
            break
        posicao = find(COD_ESQ, list[posicao][3])

if (is_fila == True) and (is_pilha == True):
    print("ambas")
elif (is_fila == True) and (is_pilha == False):
    print("fila")
elif (is_fila == False) and (is_pilha == True):
    print("pilha")
