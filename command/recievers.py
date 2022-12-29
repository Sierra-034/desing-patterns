class Reciever:
    """
    The reciever classes contain some important business logic. They know how to
    perform all kinds of operations, associated with carrying out a request. In
    fact, any class may serve as a Reciever.
    """

    def do_something(self, a: str) -> None:
        print(f'\nReciever: Working on ({a}.)', end='')

    def do_something_else(self, b: str) -> None:
        print(f'\nReciever: Also working on ({b}.)', end='')
    