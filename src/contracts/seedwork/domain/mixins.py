from contracts.seedwork.domain.rules import BusinessRule
from contracts.seedwork.domain.exceptions import BusinessRuleException


class ValidateRules:

    def validate_rule(self, rule: BusinessRule):
        if not rule.is_valid():
            raise BusinessRuleException(rule)
