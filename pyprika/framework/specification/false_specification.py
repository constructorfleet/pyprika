from pyprika.framework.specification.nullary_composite_specification import \
    NullaryCompositeSpecification


class FalseSpecification(NullaryCompositeSpecification):

    def is_satisfied_by(self, candidate):
        return False
