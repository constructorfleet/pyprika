from pyprika.framework.specification.multary_composite_specification import \
    MultaryCompositeSpecification


class And(MultaryCompositeSpecification):

    def __and__(self, other):
        if isinstance(other, And):
            self.specifications += other.specifications
        else:
            self.specifications += (other,)
        return self

    def is_satisfied_by(self, candidate):
        satisfied = all([
            specification.is_satisfied_by(candidate)
            for specification in self.specifications
        ])
        return satisfied

    def remainder_unsatisfied_by(self, candidate):
        non_satisfied = [
            specification
            for specification in self.specifications
            if not specification.is_satisfied_by(candidate)
        ]
        if not non_satisfied:
            return None
        if len(non_satisfied) == 1:
            return non_satisfied[0]
        if len(non_satisfied) == len(self.specifications):
            return self
        return And(*non_satisfied)
