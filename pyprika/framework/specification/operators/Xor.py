from pyprika.framework.specification.binary_composite_specification import BinaryCompositeSpecification


class Xor(BinaryCompositeSpecification):

    def is_satisfied_by(self, candidate):
        return (
                self.left.is_satisfied_by(candidate) ^
                self.right.is_satisfied_by(candidate)
        )
