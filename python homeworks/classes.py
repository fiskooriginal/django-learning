class A:
    def __g():  # private method
        return 'Hello, World'

    def printHello(self):
        return f'Hello, {self.name}'

    def __init__(self, name='World'):
        self.name = name


a = A()
print(a.printHello())
a = A('Misha')
print(a.printHello())


# a = A()
# print(a._A__g())


class Mydict(dict):
    def get(self, key, default=0):
        return dict.get(self, key, default)


a = dict(a=1, b=2)
b = Mydict(a=1, b=2)

print(a.get('v'))
print(b.get('v'))
