# class is blueprint for creating new objects
# object is an instances of a class


# class Point:
#     default_color = "red"

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")


# point = Point(1, 2)
# point.draw()


# Inhertiance

from abc import ABC, abstractmethod  # this makes it abstract


class InvalidOperationError(Exception):  # custom Error
    pass


class Stream(ABC):  # make it abstract
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream already open")
        self.opened = True

    def close(self):
        if not self.close:
            raise InvalidOperationError("Stream already closed")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")


stream = FileStream()
isOpen = not stream.opened
print(isOpen)
