# 1. data-descriptors
# 2. self.__dict__['d']
# 3. non-data-descriptors

class C:
    # a non-data descriptors only has a __get__ attribute
    def __get__(self, instance, owner=None):
        print(instance)
        print(owner)
        print("hi")
        return 0


class D:
    c = C()



c = C()


d = D()

# class methods are just descriptors
d.__init__.__get__



