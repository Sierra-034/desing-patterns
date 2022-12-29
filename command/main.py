from invokers import Invoker
from commands import SimpleCommand, ComplexCommand
from recievers import Reciever

if __name__ == '__main__':
    """
    The client code can parameterize an invoker with any commands.
    """

    invoker = Invoker()
    invoker.set_on_start(SimpleCommand('Say Hi!'))
    reciever = Reciever()
    invoker.set_on_finish(ComplexCommand(
        reciever, 'Send mail', 'Save report'
    ))

    invoker.do_something_important()
