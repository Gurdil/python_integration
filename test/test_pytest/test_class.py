__author__ = 'philip_j'


# content of test_class.py
class TestClass:
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"

        class lm:
            egg = 8

            def __init__(self):
                self.check = 0

        assert hasattr(lm(), 'check')
        assert hasattr(lm, 'egg')
