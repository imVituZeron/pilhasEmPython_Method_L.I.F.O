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