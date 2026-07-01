class A:
    def __init__(self):
        self._x = 5

class B(A):
    def display(self):
        print(self._x)

obj = B()
obj.display()