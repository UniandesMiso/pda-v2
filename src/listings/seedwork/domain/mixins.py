from listings.seedwork.domain.rules import BusinessRule
from listings.seedwork.domain.exceptions import BusinessRuleException


class ValidateRules:

    def validate_rule(self, rule: BusinessRule):
        if not rule.is_valid():
            raise BusinessRuleException(rule)
