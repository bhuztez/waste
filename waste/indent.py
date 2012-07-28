from contextlib import contextmanager
from functools import wraps

from .base import Template

__all__ = ('IndentTemplate', 'indent')



class IndentTemplate(Template):

    INDENT = None


    def __init__(self, context):
        super(IndentTemplate, self).__init__(context)

        self._first_indent = True
        self._indent_level = 0
        self._has_children = None


    def _increase_indent_level(self):
        if self.INDENT:
            if not self._first_indent:
                self.emit(u'\n')
            else:
                self._first_indent = False

            self.emit(u' '*(self.INDENT*self._indent_level))

            self._indent_level += 1
            self._has_children = False


    @contextmanager
    def _decrease_indent_level(self):
        if self.INDENT:
            if self._has_children:
                self.emit(u'\n', u' '*(self.INDENT*(self._indent_level-1)))

        yield

        if self.INDENT:
            self._indent_level -= 1
            self._has_children = True



def indent(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        g = func(self, *args, **kwargs)

        self._increase_indent_level()
        inner_context = g.next()

        yield inner_context

        with self._decrease_indent_level():
            try:
                g.next()
            except StopIteration:
                pass

    return wrapper

