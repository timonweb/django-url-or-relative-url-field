from django.forms import URLField

from .validators import url_or_relative_url_validator


class URLOrRelativeURLFormField(URLField):
    default_validators = [url_or_relative_url_validator]

    def to_python(self, value):
        value = super().to_python(value)
        if value:
            if value.startswith('http:///'):
                # If value starts with ``http:///`` (followed by 3 slashes)
                # that means user provided a relative url and a parent ``URLField`` class
                # has appended a ``http://`` to it.
                # We need to strip it out and convert to correct relative url
                # before we pass it down the line.
                value = value[7:]
        return value
