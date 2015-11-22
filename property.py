"""
Property

Allows the ability of creating properties of a class that looks and acts like a
normal attribute, except that you provide methods that control access to the
attribute.

    property(fget=None, fset=None, fdel=None, doc=None)

where, fget is function to get value of the attribute, fset is function to set
value of the attribute, fdel is function to delete the attribute and doc is a
string (like a comment). As seen from the implementation, these function
arguments are optional. The above construct can also be implemented as
decorators @property.

One of the benefits of using properties is that if your code changes in the
future, you can just modify your class to add getters and setters for the data
without changing the interface, so you don't have to find everywhere in your
code where that data is accessed and change that too. Provides a form of
encapsulation.

Google Python styleguide:
https://google.github.io/styleguide/pyguide.html#Properties

"""


class A(object):
    """
    Example of defining a property 'x' in a class with getters and setters
    """

    def __init__(self):
        self._x = None

    def __getx(self):
        return self._x

    def __setx(self, value):
        self._x = value

    def __delx(self):
        del self._x

    x = property(__getx, __setx, __delx, "I'm the 'x' property of class A.")


class B(object):
    """
    Example of defining a property 'x' in a class that is only read-only.
    fset is not definied in the property.
    """

    def __init__(self):
        self._x = None

    def __getx(self):
        return self._x

    def __delx(self):
        del self._x

    x = property(fget=__getx, fdel=__delx, doc="I'm the read-only 'x' property of class B.")
    # x = property(__getx, None, __delx, "I'm the read-only 'x' property of class B.")


class C(object):
    """
    Example of defining a property 'x' in a class with getters and setters using
    decorators.
    """

    def __init__(self):
        self._x = None

    @property
    def x(self):
        "I'm the 'x' property of class C."
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


class D(object):
    """
    Example of defining a read-only property 'x' in a class using decorators.
    """

    def __init__(self):
        self._x = None

    @property
    def x(self):
        "I'm the 'x' property."
        return self._x

    @x.deleter
    def x(self):
        del self._x


def main():
    a = A()
    # calls __setx in property
    a.x = 5
    # calls __getx in property
    print a.x

    b = B()
    # should fail since no __setx was definied
    # b.x = 10
    print b.x

    c = C()
    c.x = 5
    print c.x

    d = D()
    # should fail since no @x.setter was definied
    # d.x = 5
    print d.x


if __name__ == '__main__':
    main()
