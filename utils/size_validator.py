from django.core.exceptions import ValidationError


def validate_max_size(image_object):
    factor = 2
    if image_object.size > factor * 1024 * 1024:
        raise ValidationError(f"The max file size should be {factor} MB.")
