from abc import ABC, abstractmethod

from recievers import Reciever

class Command(ABC):
    """
    The command interface declares a method for executing a command.
    """

    @abstractmethod
    def execute(self) -> None:
        pass

class SimpleCommand(Command):
    """
    Some commands can implement simple operations on their own.
    """

    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(
            f'SimpleCommand: See, I can do simple things like printing',
            f'{self._payload}'
        )

class ComplexCommand(Command):
    """
    However, some commands can delegate more complex operations
    to other objects, called "recievers".
    """

    def __init__(self, reciever: Reciever, a: str, b: str) -> None:
        """
        Complex commands can accept one or several reciever objects
        along with any context data via the constructor
        """

        self._reciever = reciever
        self._a = a
        self._b = b

    def execute(self) -> None:
        """
        Commands can delegate to any methods of a reciever
        """

        print('ComplexCommand: Complex stuff should be done by a reciever object', end='')
        self._reciever.do_something(self._a)
        self._reciever.do_something_else(self._b)
