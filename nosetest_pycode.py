from pycode import pyfunc

def test_pyfunc_python():
  assert pyfunc('Guido van Rossum','Python') == 'Guido van Rossum, known for Python'

def test_pyfunc_perl():
  assert pyfunc('Larry Wall','Perl') == 'Larry Wall, known for Perl'

def test_pyfunc_ruby():
  assert pyfunc('Yukihiro Matsumoto','Ruby') == 'Yukihiro Matsumoto, known for Ruby'

