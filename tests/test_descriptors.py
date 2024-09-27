class MyDescriptor:
    def __get__(self, instance, owner=None):
        print("getting")
        print(instance, owner)
        ...

    def __set_name__(self, owner, name):
        print("setting name")
        print(owner)
        print(name)

    def __set__(self, obj, value):
        ...


class D:
    c = MyDescriptor()

def test_access():
    class F:
        f = MyDescriptor()


    d = D()

    print(d.c)

