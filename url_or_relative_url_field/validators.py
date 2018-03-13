from django.core import validators


def url_or_relative_url_validator(value):
    if value.startswith('/'):
        # We transform a relative url into a fictitious absolute url
        # so we could use built-in url validator.
        value = 'http://example.com' + value
    return validators.URLValidator()(value)
