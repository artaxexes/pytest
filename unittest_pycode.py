import unittest
from pycode import pyfunc

class TestPyCode(unittest.TestCase):

  def setUp(self):
    pass

  def test_pyfunc_python(self):
    self.assertEqual(pyfunc('Guido van Rossum','Python'),'Guido van Rossum, known for Python')

  def test_pyfunc_perl(self):
    self.assertEqual(pyfunc('Larry Wall','Perl'),'Larry Wall, known for Perl')

  def test_pyfunc_ruby(self):
    self.assertEqual(pyfunc('Yukihiro Matsumoto', 'Ruby'),'Yukihiro Matsumoto, known for Ruby')

if __name__ == '__main__':
    unittest.main()
