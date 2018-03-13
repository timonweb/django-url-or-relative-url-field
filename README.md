# Django URL or Relative URL Field

This package extends default Django URLField to support relative URLs.


## Installation

1. Install the python package django-url-or-relative-url-field from pip:

    ``pip install django-url-or-relative-url-field``

    Alternatively, you can install download or clone this repo and call ``pip install -e .``.
  
2. Add to INSTALLED_APPS in your **settings.py**:

    `'url_or_relative_url_field',`
  
## Usage  
  
Add field to the model:

```python
from django.db import models
from url_or_relative_url_field.fields import URLOrRelativeURLField

class Redirect(models.Model):
   url = URLOrRelativeURLField()
```

Now your model will accept both absolute and relative URLs into the ``url`` field.
