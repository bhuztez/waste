from ..indent import IndentTemplate

__all__ = ('HtmlTemplate',)


class HtmlTemplate(IndentTemplate):
    from .tags import *

