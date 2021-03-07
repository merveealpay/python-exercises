class A:
    def show(self):
        print("show of A called")


class B(A):
    def show(self):
        print("show of B called")


class C(A):
    def show(self):
        print("show of C called")


class D(B, C):
    def show(self):
        super(D, self).show()
        print("show of D called")


x = D()  # Creating object
x.show()
