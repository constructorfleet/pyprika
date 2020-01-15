from pyprika.framework.specification.multary_composite_specification import MultaryCompositeSpecification


class Or(MultaryCompositeSpecification):

    def __or__(self, other):
        if isinstance(other, Or):
            self.specifications += other.specifications
        else:
            self.specifications += (other,)
        return self

    def is_satisfied_by(self, candidate):
        satisfied = any([
            specification.is_satisfied_by(candidate)
            for specification in self.specifications
        ])
        return satisfied
