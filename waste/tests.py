import unittest

from .html import HtmlTemplate
from .html.filters import escape



class TestTemplate(HtmlTemplate):

    INDENT = 2


    def render(self):
        with self.html() as self:
            with self.head() as self:
                with self.title() as self:
                    self.emit(u"Hello, ", self[u"name"]|escape(), u"!")
            with self.body() as self:
                with self.h1() as self:
                    self.emit(u"Hello, ", self[u"name"]|escape(), u"!")



class HtmlTemplateTestCase(unittest.TestCase):


    def test_render(self):
        self.assertEqual(
            unicode(TestTemplate({u"name": u"world"})),
            u"""<html>
  <head>
    <title>Hello, world!</title>
  </head>
  <body>
    <h1>Hello, world!</h1>
  </body>
</html>""")



def suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)



if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

