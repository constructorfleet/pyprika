from pyprika.framework.specification.unary_composite_specification import \
    UnaryCompositeSpecification


class Invert(UnaryCompositeSpecification):

    def is_satisfied_by(self, candidate):
        return not self.specification.is_satisfied_by(candidate)
