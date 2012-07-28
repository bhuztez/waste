from ..utils import tag
from ..indent import indent

__all__ = ('html', 'head', 'title', 'body', 'h1', 'p')


@tag
@indent
def html(self):
    self.emit(u'<html>')
    yield
    self.emit(u'</html>')


@tag
@indent
def head(self):
    self.emit(u'<head>')
    yield
    self.emit(u'</head>')


@tag
@indent
def title(self):
    self.emit(u'<title>')
    yield
    self.emit(u'</title>')


@tag
@indent
def body(self):
    self.emit(u'<body>')
    yield
    self.emit(u'</body>')


@tag
@indent
def h1(self):
    self.emit(u'<h1>')
    yield
    self.emit(u'</h1>')


@tag
@indent
def p(self):
    self.emit(u'<p>')
    yield
    self.emit(u'</p>')

