from contextlib import contextmanager
from functools import wraps

__all__ = ('filter', 'tag', 'ContextWrapper')



class ContextWrapper(object):


    def __init__(self, value):
        self.value = value


    def __unicode__(self):
        return unicode(self.value)


    def __getattr__(self, name):
        return self.__class__(getattr(self.value, name))


    def __getitem__(self, name):
        return self.__class__(self.value[name])        


    def __call__(self, *args, **kwargs):
        return self.__class__(self.value(*args, **kwargs))



class Filter(object):


    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs


    def __ror__(self, other):
        return other.__class__(self.func(other.value, *self.args, **self.kwargs))



def filter(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        return Filter(func, *args, **kwargs)

    return wrapper



def tag(func):

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        g = func(self, *args, **kwargs)
        inner_context = g.next()

        if inner_context is None:
            inner_context = self

        yield inner_context

        try:
            g.next()
        except StopIteration:
            pass

    return contextmanager(wrapper)
