from django.core.exceptions import ValidationError


def positive_number(value):
    result = value >= 0
    if not result:
        raise ValidationError('Quantity must be positive number')