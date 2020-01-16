from pyprika.framework.specifications import MultaryCompositeSpecification
from pyprika.framework.specifications.binary_composite_specification import \
    BinaryCompositeSpecification
from pyprika.framework.specifications.multary_composite_specification import \
    MultaryCompositeSpecification
from pyprika.framework.specifications.unary_composite_specification import \
    UnaryCompositeSpecification


class Specification:

    def __and__(self, other):
        return And(self, other)

    def __or__(self, other):
        return Or(self, other)

    def __xor__(self, other):
        return Xor(self, other)

    def __invert__(self):
        return Invert(self)

    def is_satisfied_by(self, candidate):
        raise NotImplementedError()

    def remainder_unsatisfied_by(self, candidate):
        if self.is_satisfied_by(candidate):
            return None
        else:
            return self


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


class Invert(UnaryCompositeSpecification):

    def is_satisfied_by(self, candidate):
        return not self.specification.is_satisfied_by(candidate)


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


class Xor(BinaryCompositeSpecification):

    def is_satisfied_by(self, candidate):
        return (
                self.left.is_satisfied_by(candidate) ^
                self.right.is_satisfied_by(candidate)
        )
