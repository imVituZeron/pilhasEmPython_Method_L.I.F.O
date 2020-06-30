from __future__ import annotations
from typing import List, Any

class Stack:
    def __init__(self) -> None:
        self.__data: List[Any] = []
        self.__index = 0

    def push(self, item: Any) -> None:
        self.__data.append(item)

    def pop(self) -> Any:
        return self.__data.pop()

    def peek(self) -> Any:
        if not self.__data:
            return []
        
        return self.__data[-1]

    def repr(self) -> str:
        return f'{self.__class__.__name__}({self.__data})'

    def __iter__(self) -> Stack:
        self.__index = len(self.__data)
        return self

    def __next__(self) -> Any:
        if self.__index == 0:
            raise StopIteration

        self.__index -= 1
        return self.__data[self.__index]

    def __bool__(self) -> bool:
        return bool(self.__data)

if __name__ == "__main__":
    stack = Stack()

    stack.push('A')
    stack.push('B')
    stack.push('C')

    for item in stack:
        print(item)

    while stack:
        print(stack.pop())