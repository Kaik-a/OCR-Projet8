from typing import Any

from django.template.defaultfilters import stringfilter
from django.template.defaulttags import register


@register.filter(name='stringify')
@stringfilter
def stringify(to_convert: Any):
    return to_convert
