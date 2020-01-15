from abc import ABC

from pyprika.framework.specification.composite_specification import CompositeSpecification


class MultaryCompositeSpecification(CompositeSpecification, ABC):

    def __init__(self, *specifications):
        self.specifications = specifications
