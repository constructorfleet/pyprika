from pyprika.framework.specification.operators.And import And
from pyprika.framework.specification.operators.Invert import Invert
from pyprika.framework.specification.operators.Or import Or
from pyprika.framework.specification.operators.Xor import Xor


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
