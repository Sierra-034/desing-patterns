from abc import ABC, abstractmethod

class Visitor(ABC):
    """
    The visitor interface declares a set of visiting methods that correspond to
    componet classes. The signature of a visiting method allows the visitor to
    identify the exact class of the component that it's dealing with.
    """
    
    @abstractmethod
    def visit_concrete_component_a(self, element) -> None:
        pass

    @abstractmethod
    def visit_concrete_component_b(self, element) -> None:
        pass


"""
Concrete visitors implement several versions of the same algorithm, which can
work with all concrete component classes.

You can experience the biggest benefist of the visitor when using it with
a complex object structure, such as a Composite tree. In this case, it might be
helpful to store some intermediate state of the algorithm while executing
visitor's methods over various objects of the structure.
"""

class ConcreteVisitor1(Visitor):
    def visit_concrete_component_a(self, element) -> None:
        print(f'{element.exclusive_method_of_concrete_component_a()} + ConcreteVisitor1')
    
    def visit_concrete_component_b(self, element) -> None:
        print(f'{element.special_method_of_concrete_component_b()} + ConcreteVisitor1')

class ConcreteVisitor2(Visitor):
    def visit_concrete_component_a(self, element) -> None:
        print(f'{element.exclusive_method_of_concrete_component_a()} + ConcreteVisitor2')

    def visit_concrete_component_b(self, element) -> None:
        print(f'{element.special_method_of_concrete_component_b()} + ConcreteVisitor2')
