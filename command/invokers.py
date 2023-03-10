from commands import Command

class Invoker:
    """
    The invoker is associated with one or several commands. It sends
    a request to the command.
    """

    _on_start = None
    _on_finish = None

    """
    Initialize commands.
    """

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self) -> None:
        """
        The invoker does not depend on concrete command or reciever classes. The
        Invoker passes a request to a reciever indirectly, by executing a
        command.
        """

        print('Invoker: Does anybody want something done before I begin?')
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print('Invoker: ...doing something really important...')

        print('Invoker: Does anybody want something done before I finish?')
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()
    