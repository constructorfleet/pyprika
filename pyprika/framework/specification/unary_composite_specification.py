from abc import ABC

from pyprika.framework.specification.composite_specification import CompositeSpecification


class UnaryCompositeSpecification(CompositeSpecification, ABC):

    def __init__(self, specification):
        self.specification = specification
