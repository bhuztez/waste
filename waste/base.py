try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

from .utils import ContextWrapper

__all__ = ('Template',)



class Template(object):

    CONTEXT_WRAPPER = ContextWrapper


    def __init__(self, context):
        self._buf = StringIO()
        self._cache = None
        self._context = context


    def __repr__(self):
        return '<%s %s>'%(self.__class__.__name__, repr(self._context))


    def __unicode__(self):
        if self._cache is None:
            self.render()
            self._cache = self._buf.getvalue()
            self._buf = None

        return self._cache


    def __getitem__(self, name):
        return self.CONTEXT_WRAPPER(self._context[name])


    def emit(self, *args):
        for arg in args:
            self._buf.write(unicode(arg))


    def render(self):
        pass


