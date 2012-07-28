from ..utils import filter

@filter
def escape(value):
    return unicode(value).replace(u'&', u'&amp;').replace(u'<', u'&lt;').replace(u'>', u'&gt;').replace(u'"', u'&quot;')

