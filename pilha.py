from typing import List

stack: List[str] = []

stack.append('A')
stack.append('B')
stack.append('C')

# removendo item da pilha com os métodos da lista
#top_item = stack.pop() # Removendo C
#top_item = stack.pop() # removendo B

#com o FOR:
for item in stack[::-1]:
    print(item)

# com WHILE:
while stack:
    item = stack.pop()
    print(item)