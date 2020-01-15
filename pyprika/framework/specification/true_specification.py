from pyprika.framework.specification.nullary_composite_specification import NullaryCompositeSpecification


class TrueSpecification(NullaryCompositeSpecification):

    def is_satisfied_by(self, candidate):
        return True
