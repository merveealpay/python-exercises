class X:
    def met(self):
        print("X OK")


class Y:
    def met(self):
        print("Y OK")


class Z(X, Y):
    def met(self):
        super(X, self).met()


class A(Z):
    def met(self):
        super(A, self).met()


object = A()
object.met()

#Y OK