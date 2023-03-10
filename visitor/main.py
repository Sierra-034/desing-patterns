from typing import List

from components import Component, ConcreteComponentA, ConcreteComponentB
from visitors import Visitor, ConcreteVisitor1, ConcreteVisitor2

def client_code(components: List[Component], visitor: Visitor):
    """
    The client code can run visitor operations over any set of elements without
    figuring out their concrete classes. The accept operation directs a call to
    the appropiate operation in the visitor object.
    """

    for component in components:
        component.accept(visitor)


if __name__ == '__main__':
    components = [ConcreteComponentA(), ConcreteComponentB()]

    print('The client code works with all visitors via de base Visitor interface:')
    visitor1 = ConcreteVisitor1()
    client_code(components, visitor1)

    print('It allows the same client code to work with different types of visitors:')
    visitor2 = ConcreteVisitor2()
    client_code(components, visitor2)
