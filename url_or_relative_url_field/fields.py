from django.db import models
from django.utils.translation import ugettext_lazy as _

from .forms import URLOrRelativeURLFormField
from .validators import url_or_relative_url_validator


class URLOrRelativeURLField(models.URLField):
    description = _("URL or path")
    default_validators = [url_or_relative_url_validator]

    # def __init__(self, verbose_name=None, name=None, **kwargs):
    #     super().__init__(verbose_name, name, **kwargs)
    #     self.validators.append(url_or_relative_url_validator)

    def formfield(self, **kwargs):
        # As with CharField, this will cause URL validation to be performed
        # twice.
        defaults = {
            'form_class': URLOrRelativeURLFormField,
        }
        defaults.update(kwargs)
        return super().formfield(**defaults)
