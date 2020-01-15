from abc import ABC

from pyprika.framework.specification.composite_specification import CompositeSpecification


class BinaryCompositeSpecification(CompositeSpecification, ABC):

    def __init__(self, left, right):
        self.left = left
        self.right = right
